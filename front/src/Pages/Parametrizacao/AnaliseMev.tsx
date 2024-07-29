import { useEffect, useState } from "react";
import { PageModel } from "../../Components/PageModel";
import { PiPlus } from "react-icons/pi";
import { CRUDTable } from "../../Components/CRUDTable";
import { LateralMenu } from "../../Components/LateralMenu";
import { baseURL } from "../../config/AxiosConfig";

type formAnaliseData = {
    id_analises_mev: 0,
    tipo_cristal: string,
    tamanho_cristal: string,
    magnificacao_mev: string,
    tensao_mev: string,
    wd_mev: string
}
export const AnaliseMev = () => {

    const [data, setData] = useState<formAnaliseData[]>();
    const [dataForm, setDataForm] = useState<formAnaliseData>();
    const [feedback, setFeedback] = useState<boolean>(false);
    const [feedbackError, setFeedbackError] = useState<boolean>(false);

    const remove = (element: any) => {
        baseURL.delete(`analise_mev/${element}`).then(() => {
            setFeedback(!feedback);
        }).catch(() => {
            setFeedbackError(!feedbackError);
        })

    }
    const edit = (element: any) => {
        let retorno: formAnaliseData | undefined = data?.find(e => e.id_analises_mev == element);
        if (retorno) {
            document.getElementById("modalButton")?.click();
            setDataForm(retorno)
        }
    }
    const submitForm = (form: any) => {
        form.preventDefault();
        let retorno: formAnaliseData = {
            id_analises_mev: form.target[0].value,
            tipo_cristal: form.target[1].value,
            tamanho_cristal: form.target[2].value,
            magnificacao_mev: form.target[3].value,
            tensao_mev: form.target[4].value,
            wd_mev: form.target[5].value
        }

        document.getElementById("CloseModalButton")?.click();
        if (data?.find(e => e.id_analises_mev == retorno.id_analises_mev)) {
            baseURL.put('analise_mev', retorno).then(response => {
                if (response.status == 200)
                    setFeedback(!feedback);
            }).catch(() => {
                setFeedbackError(!feedbackError);
            })
        } else {
            baseURL.post('analise_mev', retorno).then(() => {
                setFeedback(!feedback);
            }).catch(() => {

                setFeedbackError(!feedbackError);
            })
        }
    }
    const closeModal = () => {
        (document.getElementById("ModalForm") as HTMLFormElement)?.reset();
        setDataForm({} as formAnaliseData);
    }
    const getData = () => {
        baseURL.get('analise_mev').then((response) => {
            setData(response.data);
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
                <div className="modal-box flex-col flex items-center">
                    <form id='ModalForm' className="form-control rounded-xl p-10" onSubmit={(form) => { submitForm(form) }}>
                        <h3 className="text-lg font-bold mb-10 self-center">Cadastro de Análise Mev</h3>
                        <label className="input input-bordered text-white  bg-white flex items-center gap-2 mb-5">
                            id_analises_mev |
                            <input type="text" className="grow  text-white" placeholder="..." defaultValue={dataForm?.id_analises_mev} disabled />
                        </label>

                        <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5">
                            tipo_cristal |
                            <input type="text" className="grow text-black" placeholder="..." defaultValue={dataForm?.tipo_cristal} required />
                        </label>

                        <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5">
                            tamanho_cristal |
                            <input type="text" className="grow text-black" placeholder="..." defaultValue={dataForm?.tamanho_cristal} required />
                        </label>

                        <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5">
                            magnificacao_mev |
                            <input type="text" className="grow text-black" placeholder="..." defaultValue={dataForm?.magnificacao_mev} required />
                        </label>

                        <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5">
                            tensao_mev |
                            <input type="text" className="grow text-black" placeholder="..." defaultValue={dataForm?.tensao_mev} required />
                        </label>

                        <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5">
                            wd_mev |
                            <input type="text" className="grow text-black" placeholder="..." defaultValue={dataForm?.wd_mev} required />
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
                        <a className="text-2xl text-black font-semibold"> Análise Mev</a>
                        <label id="modalButton" htmlFor="my_modal_6" className="hover:bg-green-500 transition-all hover:w-16 btn btn-circle btn-outline border-black text-black"><PiPlus /></label>
                    </div>
                    {data ?
                        <CRUDTable idColumnName='id_analises_mev' data={data as object[]} deleteFunction={remove} editFunction={edit} />
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