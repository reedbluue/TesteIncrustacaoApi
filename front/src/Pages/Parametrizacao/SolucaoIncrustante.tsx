import { useEffect, useState } from "react";
import { PageModel } from "../../Components/PageModel";
import { PiPlus } from "react-icons/pi";
import { CRUDTable } from "../../Components/CRUDTable";
import { LateralMenu } from "../../Components/LateralMenu";
import { formReagenteData } from "./Reagente";
import { baseURL } from "../../config/AxiosConfig";
import { MultiSelect } from "react-multi-select-component";
type formData = {
    id_uniao: number,
    id_solucao: number,
    nome: string,
    tipo_preparo: string,
    reagentes: Array<formReagenteData>
}
type selectedType = {
    label: string,
    value: number
}
type concatDataType = {
    id_solucao: number,
    nome: string,
    tipoPreparo: string,
    reagente: string
}
export const SolucaoIncrustante = () => {
    const [data, setData] = useState<formData[]>();
    const [dataConcat, setDataConcat] = useState<concatDataType[]>();
    const [dataForm, setDataForm] = useState<formData>();
    const [feedback, setFeedback] = useState<boolean>(false);
    const [feedbackError, setFeedbackError] = useState<boolean>(false);
    const [options, setOptions] = useState([]);
    const [selected, setSelected] = useState<Array<selectedType>>([]);

    const remove = (element: any) => {
        baseURL.delete(`solucao_incrustante/${element}`).then(() => {
            setFeedback(!feedback);
            getData();
        }).catch(() => {
            setFeedbackError(!feedbackError);
        })
    }
    const edit = (element: any) => {
        let retorno: formData | undefined = data?.find(e => e.id_solucao == element);
        if (retorno) {
            document.getElementById("modalButton")?.click();
            setDataForm(retorno)
            let selectedFormated: selectedType[] = retorno.reagentes.map(e => { return { value: e.id_reagente, label: e.nome } as selectedType })
            setSelected(selectedFormated);
        }
    }
    const submitForm = (form: any) => {
        form.preventDefault();
        let retorno = {
            id_solucao: form.target[0].value,
            nome: form.target[1].value,
            tipo_preparo: form.target[2].value
        }
        if (selected.length) {

            document.getElementById("CloseModalButton")?.click();
            if (data?.find(e => e.id_solucao == retorno.id_solucao)) {
                baseURL.put('solucao_incrustante', retorno).then(response => {
                    if (response.status == 200) {
                        let reagentesPut = { id_solucao: retorno.id_solucao, ids_reagentes: selected.map(e => e.value) }
                        baseURL.put('solucao_incrustante/reagentes', reagentesPut).then(regenteResponse => {
                            if (regenteResponse.status == 200)
                                setFeedback(!feedback);
                        })
                    }
                }).catch((e) => {
                    console.log(e)
                    setFeedbackError(!feedbackError);
                })
            } else {
                baseURL.post('solucao_incrustante', retorno).then((response) => {
                    let reagentesPut = { id_solucao: response.data.id_solucao, ids_reagentes: selected.map(e => e.value) }
                    baseURL.put('solucao_incrustante/reagentes', reagentesPut).then(regenteResponse => {
                        if (regenteResponse.status == 200)
                            setFeedback(!feedback);
                    })

                }).catch((e) => {
                    console.log(e.response.data)
                    setFeedbackError(!feedbackError);
                })
            }
        }
    }
    const closeModal = () => {
        (document.getElementById("ModalForm") as HTMLFormElement)?.reset();
        setDataForm({} as formData);
    }
    const getData = () => {
        baseURL.get('solucao_incrustante').then((response) => {
            setData(response.data);
        })
        baseURL.get('reagente').then((response) => {
            let data: formReagenteData[] = response.data;
            let optionsdata = data.map(e => { return { label: e.nome, value: e.id_reagente } })
            setOptions(optionsdata as never[]);
        })

    }
    useEffect(() => {
        getData();
    }, [])
    useEffect(() => {
        if (data) {
            let matriz = data?.map(element => element.reagentes.map(line => { return { id_solucao: element.id_solucao, nome: element.nome, tipoPreparo: element.tipo_preparo, reagente: line.nome } }));
            if (matriz.length)
                setDataConcat(matriz.reduce((list, sub) => list.concat(sub)) as concatDataType[])
        }
    }, [data])

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
                <div className="modal-box flex-col flex items-center">
                    <form id='ModalForm' className="form-control rounded-xl p-10" onSubmit={(form) => { submitForm(form) }}>
                        <h3 className="text-lg font-bold mb-10 self-center">Cadastro de Solução Incrustante</h3>
                        <label className="input input-bordered text-white  bg-white flex items-center gap-2 mb-5">
                            id solucao incrustante |
                            <input type="text" className="grow  text-white" placeholder="..." defaultValue={dataForm?.id_solucao} disabled />
                        </label>
                        <label className="input input-bordered text-gray-400  bg-white flex items-center gap-2 mb-5">
                            Nome |
                            <input type="text" className="grow  text-black" placeholder="..." defaultValue={dataForm?.nome} required />
                        </label>
                        <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5">
                            tipo preparo |
                            <input type="text" className="grow text-black" placeholder="..." required defaultValue={dataForm?.tipo_preparo} />
                        </label>
                        <label id="Select" className=" input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5">
                            Reagente
                            <MultiSelect className="w-full mr-1"
                                options={options}
                                value={selected}
                                onChange={setSelected}
                                labelledBy="Select"
                            />
                        </label>
                        <div className="modal-action justify-between w-full">
                            <label id='CloseModalButton' htmlFor="my_modal_6" onClick={closeModal} className="btn btn-error">Fechar</label>
                            <button className="btn btn-success text-white" >Cadastrar</button>
                        </div>
                    </form>
                </div>
            </div>
            {/* Conteudo da página */}
            <div className=' flex flex-col h-full lg:flex-row md:justify-center'>
                <LateralMenu />
                <div className="h-full bg-[#D9D9D9] w-full lg:w-5/6 rounded-3xl p-20 ">
                    <div className=" justify-between items-center flex border-gray-600  p-2">
                        <a className="text-2xl text-black font-semibold">Solução Incrustante</a>
                        <label id="modalButton" htmlFor="my_modal_6" className="hover:bg-green-500 transition-all hover:w-16 btn btn-circle btn-outline border-black text-black"><PiPlus /></label>
                    </div>
                    {dataConcat ?
                        <CRUDTable idColumnName='id_solucao' data={dataConcat as object[]} deleteFunction={remove} editFunction={edit} />
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
                }
            </div>

        </PageModel>
    )
}