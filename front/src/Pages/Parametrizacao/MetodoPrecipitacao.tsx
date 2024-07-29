import { useEffect, useState } from "react";
import { PageModel } from "../../Components/PageModel";
import { PiPlus } from "react-icons/pi";
import { CRUDTable } from "../../Components/CRUDTable";
import { LateralMenu } from "../../Components/LateralMenu";
import { baseURL } from "../../config/AxiosConfig";

type formMetodoData = {
    id_metodo_pr: number,
    nome: string,
    valor: string,
}
export const MetodoPrecipitacao = () => {
    
    const [data, setData] = useState<formMetodoData[]>();
    const [dataForm, setDataForm] = useState<formMetodoData>();
    const [feedback, setFeedback] = useState<boolean>(false);
    const [feedbackError, setFeedbackError] = useState<boolean>(false);

    const remove = (element: any) => {
        baseURL.delete(`metodo_precipitacao/${element}`).then(() => {
            setFeedback(!feedback);
    }).catch(() => {
        setFeedbackError(!feedbackError);
    })

    }
    const edit = (element: any) => {
        let retorno: formMetodoData | undefined = data?.find(e => e.id_metodo_pr == element);
        if (retorno) {
            document.getElementById("modalButton")?.click();
            setDataForm(retorno)
        }
    }
    const submitForm = (form: any) => {
        form.preventDefault();
        let retorno: formMetodoData = {
            id_metodo_pr: form.target[0].value,
            nome: form.target[1].value,
            valor: form.target[2].value
        }
       
        document.getElementById("CloseModalButton")?.click();
        if (data?.find(e => e.id_metodo_pr == retorno.id_metodo_pr)) {
            baseURL.put('metodo_precipitacao', retorno).then(response => {
                if (response.status == 200)
                    setFeedback(!feedback);
            }).catch((e) => {
                console.log(e)
                setFeedbackError(!feedbackError);
            })
        } else {
            baseURL.post('metodo_precipitacao', retorno).then(() => {
                setFeedback(!feedback);
            }).catch((e) => {
                console.log(e)
                setFeedbackError(!feedbackError);
            })
        }
    }
    const closeModal = () => {
        (document.getElementById("ModalForm") as HTMLFormElement)?.reset();
        setDataForm({} as formMetodoData);
    }
    const getData = () => {
        baseURL.get('metodo_precipitacao').then((response) => {
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
                        <h3 className="text-lg font-bold mb-10 self-center">Cadastro de Método de Precipitação</h3>
                        <label className="input input-bordered text-white  bg-white flex items-center gap-2 mb-5">
                            id Método |
                            <input type="text" className="grow  text-white" placeholder="..." defaultValue={dataForm?.id_metodo_pr} disabled />
                        </label>
                        <label className="input input-bordered text-gray-400  bg-white flex items-center gap-2 mb-5">
                            Nome |
                            <input type="text" className="grow  text-black" placeholder="..." defaultValue={dataForm?.nome} required />
                        </label>
                        <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5">
                            Valor |
                            <input type="text" className="grow text-black" placeholder="..." required defaultValue={dataForm?.valor} />
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
                        <a className="text-2xl text-black font-semibold">Método de Precipitação</a>
                        <label id="modalButton" htmlFor="my_modal_6" className="hover:bg-green-500 transition-all hover:w-16 btn btn-circle btn-outline border-black text-black"><PiPlus /></label>
                    </div>
                    {data ?
                        <CRUDTable idColumnName='id_metodo_pr' data={data as object[]} deleteFunction={remove} editFunction={edit} />
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