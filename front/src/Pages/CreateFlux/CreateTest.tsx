import { useState, useEffect } from "react";
import { PageModel } from "../../Components/PageModel";
import { PiPlus } from "react-icons/pi";
import { CRUDTable } from "../../Components/CRUDTable";
import { LateralMenu } from "../../Components/LateralMenu";
import { baseURL } from "../../config/AxiosConfig";
import CSVReader from 'react-csv-reader'
type formData = {
    id_teste: number,
    operador: string,
    regime_escoamento: string,
    rugosidade: string,
    coeficiente: string,
    metodo_teste: string,
    ph_solucao: string,
    data_inicio: string | null,
    data_fim: string | null,
    metodo_incrustacao_id: number,
    solucao_limpeza_id: number,
    metodo_precipitacao_id: number,
    solucao_incrustante_id: number,
    ferramenta_us_id: number
}
type opt = {
    label: string,
    value: string
}
type medida = {
    pressao_incrustacao: string,
    pressao_agua: string,
    temp_agua_quente_entrada: string,
    temp_agua_quente_saida: string,
    temp_agua_fria_entrada: string,
    temp_agua_fria_saida: string,
    delta_t_agua_quente: string,
    delta_t_agua_fria: string,
    vazao_agua_fria: string,
    vazao_agua_quente: string,
    vazao_reagentes: string,
    data_coleta: string,
    id_teste: number
}
export const CreateTest = () => {
    const [data, setData] = useState<formData[]>();
    const [dataCSV, setDataCSV] = useState<object>();
    const [dataForm, setDataForm] = useState<formData>();
    const [feedback, setFeedback] = useState<boolean>(false);
    const [feedbackError, setFeedbackError] = useState<boolean>(false);
    const [metodoIncrustacaoOpt, setMetodoIncrustacaoOpt] = useState<opt[]>();
    const [solucaoLimpeza, setSolucaoLimpeza] = useState<opt[]>();
    const [metodoPrecipitacao, setMetodoPrecipitacao] = useState<opt[]>();
    const [solucaoIncrustante, setSolucaoIncrustante] = useState<opt[]>();
    const [ferramentaUs, setFerramentaUs] = useState<opt[]>();

    const remove = (element: any) => {
        baseURL.delete(`teste/${element}`).then(() => {
            setFeedback(!feedback);
        }).catch(() => {
            setFeedbackError(!feedbackError);
        })

    }
    const edit = (element: any) => {
        let retorno: formData | undefined = data?.find(e => e.id_teste == element);
        if (retorno) {
            document.getElementById("modalButton")?.click();
            setDataForm(retorno)
        }
    }
    const submitForm = (form: any) => {
        form.preventDefault();

        if (form.nativeEvent.submitter.name == 'Iniciar') {
            console.log(form.target[8].value == '');
            if (form.target[8].value == '') {
                form.target[7].value = new Date().toISOString();
            } else {
                setFeedbackError(!feedbackError);
            }
        }
        if (form.nativeEvent.submitter.name == 'Finalizar') {
            if (form.target[7].value == '') {
                setFeedbackError(!feedbackError);
                return
            } else {
                form.target[8].value = new Date().toISOString();
            }
        }
        if (form.nativeEvent.submitter.name == 'Cadastrar') {
            form.target[8].value = null;
            form.target[7].value = null;
        }
        let retorno: formData = {
            id_teste: form.target[0].value,
            operador: form.target[1].value,
            regime_escoamento: form.target[2].value,
            rugosidade: form.target[3].value,
            coeficiente: form.target[4].value,
            metodo_teste: form.target[5].value,
            ph_solucao: form.target[6].value,
            data_inicio: form.target[7].value == "" ? null : form.target[7].value,
            data_fim: form.target[8].value == "" ? null : form.target[8].value,
            metodo_incrustacao_id: form.target[9].value,
            solucao_limpeza_id: form.target[10].value,
            metodo_precipitacao_id: form.target[11].value,
            solucao_incrustante_id: form.target[12].value,
            ferramenta_us_id: form.target[13].value
        }
        document.getElementById("CloseModalButton")?.click();
        if (data?.find(e => e.id_teste == retorno.id_teste)) {
            baseURL.put('teste/', retorno).then(response => {
                if (response.status == 200)
                    setFeedback(!feedback);
            }).catch((e) => {
                console.error(e);
                setFeedbackError(!feedbackError);
            })
        } else {
            baseURL.post('teste/', retorno).then(() => {
                setFeedback(!feedback);
            }).catch((e) => {
                console.error(e);
                setFeedbackError(!feedbackError);
            })
        }
    }
    const csvFormater = (data: any) => {
        let keys = data[0];
        const jsonArray = data.slice(1).map((linha: any) => {
            const obj: any = {};
            keys.forEach((keys: any, index: any) => {
                obj[keys] = linha[index];
            });
            return obj;
        });

        setDataCSV(jsonArray);
    }
    const sendArchive = () => {
        if (dataCSV && dataForm) {
            let sendData: medida[] = dataCSV as medida[];
            sendData.forEach(data => {
                data.id_teste = dataForm.id_teste;
                baseURL.post('medida/', data).then( () => {
                    setFeedback(!feedback);
                }).catch((e) => {
                    console.error(e);
                    if (e.response.status != 422)
                        setFeedbackError(!feedbackError);
                })
            });
            document.getElementById("CloseModalButton")?.click();
        }
    }
    const closeModal = () => {
        (document.getElementById("ModalForm") as HTMLFormElement)?.reset();
        setDataForm({} as formData);
        setDataCSV(undefined)
    }
    const getData = () => {
        baseURL.get('teste/').then((response) => {
            let retorno: formData[] = response.data.map((e: any) => {
                return {
                    id_teste: e.id_teste,
                    operador: e.operador,
                    regime_escoamento: e.regime_escoamento,
                    rugosidade: e.rugosidade,
                    coeficiente: e.coeficiente,
                    metodo_teste: e.metodo_teste,
                    ph_solucao: e.ph_solucao,
                    data_inicio: e.data_inicio,
                    data_fim: e.data_fim,
                    metodo_incrustacao_id: e.metodo_incrustacao.nome,
                    solucao_limpeza_id: e.solucao_limpeza.nome,
                    metodo_precipitacao_id: e.metodo_precipitacao.nome,
                    solucao_incrustante_id: e.solucao_incrustante.nome,
                    ferramenta_us_id: e.ferramenta_us.nome
                }
            })
            setData(retorno);
        })
        baseURL.get('metodo_incrustacao').then((response) => {
            setMetodoIncrustacaoOpt(response.data.map((e: any) => { return { label: e.nome, value: e.id_metodo_in } }))
        })
        baseURL.get('solucao_limpeza').then((response) => {
            setSolucaoLimpeza(response.data.map((e: any) => { return { label: e.nome, value: e.id_solucao_limpeza } }))
        })
        baseURL.get('metodo_precipitacao').then((response) => {
            setMetodoPrecipitacao(response.data.map((e: any) => { return { label: e.nome, value: e.id_metodo_pr } }))
        })
        baseURL.get('solucao_incrustante').then((response) => {
            setSolucaoIncrustante(response.data.map((e: any) => { return { label: e.nome, value: e.id_solucao } }))
        })
        baseURL.get('ferramenta_us').then((response) => {
            setFerramentaUs(response.data.map((e: any) => { return { label: e.nome, value: e.id_ferramenta } }))
        })

    }

    useEffect(() => {
        getData();
    }, [])

    useEffect(() => {
        if (feedback) {
            setTimeout(() => {
                setFeedback(!feedback);
                getData();
            }, 1000);
        }

        if (feedbackError) {
            setTimeout(() => {
                setFeedbackError(!feedbackError)
                getData();
            }, 1000);

        }
    }, [feedback, feedbackError])

    return (
        <PageModel>
            {/* Modal de cadastro e edição */}

            <input type="checkbox" id="my_modal_6" className="modal-toggle" />
            <div className="modal " role="dialog">
                <div className="modal-box max-w-[900px]  flex flex-col items-center">
                    <h3 className="text-lg font-bold mb-10 self-center">Cadastro de Teste</h3>
                    <form id='ModalForm' className=" form-control rounded-xl p-10 flex flex-col" onSubmit={(form) => { submitForm(form) }}>
                        <div className="flex flex-row">
                            <div className="mr-9">
                                <label className="input input-bordered text-white  bg-white flex items-center gap-2 mb-5">
                                    id_teste |
                                    <input type="text" className="grow text-white" placeholder="..." defaultValue={dataForm?.id_teste} disabled />
                                </label>

                                <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5">
                                    operador |
                                    <input type="text" className="grow text-black" placeholder="..." defaultValue={dataForm?.operador} required />
                                </label>

                                <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5">
                                    regime_escoamento |
                                    <input type="text" className="grow text-black" placeholder="..." defaultValue={dataForm?.regime_escoamento} required />
                                </label>

                                <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5">
                                    rugosidade |
                                    <input type="text" className="grow text-black" placeholder="..." defaultValue={dataForm?.rugosidade} required />
                                </label>

                                <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5">
                                    coeficiente |
                                    <input type="text" className="grow text-black" placeholder="..." defaultValue={dataForm?.coeficiente} required />
                                </label>

                                <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5">
                                    metodo_teste |
                                    <input type="text" className="grow text-black" placeholder="..." defaultValue={dataForm?.metodo_teste} required />
                                </label>

                                <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5">
                                    ph_solucao |
                                    <input type="text" className="grow text-black" placeholder="..." defaultValue={dataForm?.ph_solucao} required />
                                </label>
                            </div>
                            <div className="flex flex-col w-full">


                                <label className="input input-bordered text-gray-400  bg-white flex items-center gap-2 mb-5 ">
                                    data_inicio |
                                    <input type="text" className="grow text-white text-sm" placeholder="..." defaultValue={dataForm?.data_inicio ? dataForm?.data_inicio : ''} disabled />
                                </label>

                                <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5 ">
                                    data_fim |
                                    <input type="text" className="grow text-white  text-sm" placeholder="..." defaultValue={dataForm?.data_fim ? dataForm?.data_fim : ''} disabled />
                                </label>
                                <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5 pr-0">
                                    Metodo Incrustante
                                    <select className="select select-ghost text-gray-400 bg-white  w-full" >
                                        {metodoIncrustacaoOpt ? metodoIncrustacaoOpt.map(e => <option value={e.value}>{e.label}</option>) : null}
                                    </select>
                                </label>
                                <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5 pr-0">
                                    Solução Limpeza
                                    <select className="select select-bordered text-gray-400 bg-white w-full" >
                                        {solucaoLimpeza ? solucaoLimpeza.map(e => <option value={e.value}>{e.label}</option>) : null}
                                    </select>
                                </label>
                                <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5 pr-0">
                                    Metodo Precipitação
                                    <select className="select select-bordered text-gray-400 bg-white w-full" >
                                        {metodoPrecipitacao ? metodoPrecipitacao.map(e => <option value={e.value}>{e.label}</option>) : null}
                                    </select>
                                </label>
                                <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5 pr-0">
                                    Solucao Incrustante
                                    <select className="select select-bordered text-gray-400 bg-white w-full" >
                                        {solucaoIncrustante ? solucaoIncrustante.map(e => <option value={e.value}>{e.label}</option>) : null}
                                    </select>
                                </label>
                                <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5 pr-0">
                                    Ferramenta Us
                                    <select className="select select-bordered text-gray-400 bg-white w-full" >
                                        {ferramentaUs ? ferramentaUs.map(e => <option value={e.value}>{e.label}</option>) : null}
                                    </select>
                                </label>
                            </div>
                        </div>
                        <div className="modal-action justify-between w-full">

                            <label id="CloseModalButton" htmlFor="my_modal_6" onClick={closeModal} className="btn btn-error">Fechar</label>

                            {dataForm?.data_fim == undefined ?
                                <>
                                    <button name={'Iniciar'} className="btn btn-accent text-white" >Iniciar Teste</button>
                                    <button name={'Finalizar'} className="btn btn-primary text-white" >Finalizar Teste</button>
                                    <button name={'Cadastrar'} className="btn btn-success text-white" >Cadastrar</button>
                                </> :
                                <div className="flex flex-row justify-end">
                                    <div className="self-center">
                                        <CSVReader onFileLoaded={(data) => csvFormater(data)} />
                                    </div>
                                    <p onClick={sendArchive} className="btn btn-success text-white ml-5" >Enviar arquivos</p>
                                </div>
                            }
                        </div>
                    </form>
                    {dataCSV ?
                        <div className="w-full ">
                            <CRUDTable idColumnName='id_teste' data={dataCSV as object[]} deleteFunction={() => { }} editFunction={() => { }} />
                        </div> : null}
                </div>
            </div>
            {/* Conteudo da página */}
            <div className=' flex flex-col h-full lg:flex-row md:justify-center'>
                <LateralMenu />
                <div className="h-full bg-[#D9D9D9] w-full lg:w-5/6 rounded-3xl p-20 ">
                    <div className=" justify-between items-center flex border-gray-600  p-2">
                        <a className="text-2xl text-black font-semibold">Testes</a>
                        <label id="modalButton" htmlFor="my_modal_6" className="hover:bg-green-500 transition-all hover:w-16 btn btn-circle btn-outline border-black text-black"><PiPlus /></label>
                    </div>
                    {data ?
                        <CRUDTable testePage={true} idColumnName='id_teste' data={data as object[]} deleteFunction={remove} editFunction={edit} />
                        : null
                    }
                </div>
                {
                    feedback ?
                        <div className="toast toast-end toast-bottom">
                            <div className="alert alert-success">
                                <span className="text-white">Sucesso.</span>
                            </div>
                        </div>
                        : null
                }
                {
                    feedbackError ?
                        <div className="toast toast-end toast-bottom">
                            <div className="alert alert-error">
                                <span className="text-white">error.</span>
                            </div>
                        </div>
                        : null
                }</div>


        </PageModel>
    )
}