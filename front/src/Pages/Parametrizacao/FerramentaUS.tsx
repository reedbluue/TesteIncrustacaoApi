import { useEffect, useState } from "react";
import { PageModel } from "../../Components/PageModel";
import { PiPlus } from "react-icons/pi";
import { CRUDTable } from "../../Components/CRUDTable";
import { LateralMenu } from "../../Components/LateralMenu";
import { baseURL } from "../../config/AxiosConfig";

type formFerramentaData = {
    id_ferramenta: number,
    nome: string,
    frequencia: string,
    potencia: string,
    qtd_transdutor: string,
    impedancia_ferramenta: string,
    impedancia_sistema: string,
}
export const FerramentaUS = () => {

    const [data, setData] = useState<formFerramentaData[]>();
    const [dataForm, setDataForm] = useState<formFerramentaData>();
    const [feedback, setFeedback] = useState<boolean>(false);
    const [feedbackError, setFeedbackError] = useState<boolean>(false);

    const remove = (element: any) => {
        baseURL.delete(`ferramenta_us/${element}`).then(() => {
            setFeedback(!feedback);
        }).catch(() => {
            setFeedbackError(!feedbackError);
        })

    }
    const edit = (element: any) => {
        let retorno: formFerramentaData | undefined = data?.find(e => e.id_ferramenta == element);
        if (retorno) {
            document.getElementById("modalButton")?.click();
            setDataForm(retorno)
        }
    }
    const submitForm = (form: any) => {
        form.preventDefault();

        let retorno: formFerramentaData = {
            id_ferramenta: form.target[0].value,
            nome: form.target[1].value,
            frequencia: form.target[2].value,
            potencia: form.target[3].value,
            impedancia_ferramenta: form.target[4].value,
            impedancia_sistema: form.target[5].value,
            qtd_transdutor: form.target[6].value,
        }

        document.getElementById("CloseModalButton")?.click();
        if (data?.find(e => e.id_ferramenta == retorno.id_ferramenta)) {
            baseURL.put('ferramenta_us', retorno).then(response => {
                if (response.status == 200)
                    setFeedback(!feedback);
            }).catch(() => {
                setFeedbackError(!feedbackError);
            })
        } else {
            baseURL.post('ferramenta_us', retorno).then(() => {
                setFeedback(!feedback);
            }).catch(() => {

                setFeedbackError(!feedbackError);
            })
        }
    }
    const closeModal = () => {
        (document.getElementById("ModalForm") as HTMLFormElement)?.reset();
        setDataForm({} as formFerramentaData);
    }
    const getData = () => {
        baseURL.get('ferramenta_us').then((response) => {
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
                        <h3 className="text-lg font-bold mb-10 self-center">Cadastro de Ferramenta Us</h3>
                        <label className="input input-bordered text-white  bg-white flex items-center gap-2 mb-5">
                            id Ferramenta US |
                            <input type="text" className="grow  text-white" placeholder="..." defaultValue={dataForm?.id_ferramenta} disabled />
                        </label>
                        <label className="input input-bordered text-gray-400  bg-white flex items-center gap-2 mb-5">
                            Nome |
                            <input type="text" className="grow  text-black" placeholder="..." defaultValue={dataForm?.nome} required />
                        </label>
                        <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5">
                            Frequencia |
                            <input type="text" className="grow text-black" placeholder="..." required defaultValue={dataForm?.frequencia} />
                        </label>
                        <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5">
                            Potencia |
                            <input type="text" className="grow text-black" placeholder="..." required defaultValue={dataForm?.potencia} />
                        </label>
                        <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5">
                            Impedancia ferramenta |
                            <input type="text" className="grow text-black" placeholder="..." required defaultValue={dataForm?.impedancia_ferramenta} />
                        </label>
                        <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5">
                            Impedancia sistema |
                            <input type="text" className="grow text-black" placeholder="..." required defaultValue={dataForm?.impedancia_sistema} />
                        </label>
                        <label className="input input-bordered text-gray-400 bg-white flex items-center gap-2 mb-5">
                            Quantidade de transdutor |
                            <input type="text" className="grow text-black" placeholder="..." required defaultValue={dataForm?.qtd_transdutor} />
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
                        <a className="text-2xl text-black font-semibold">Ferramenta US</a>
                        <label id="modalButton" htmlFor="my_modal_6" className="hover:bg-green-500 transition-all hover:w-16 btn btn-circle btn-outline border-black text-black"><PiPlus /></label>
                    </div>
                    {data ?
                        <CRUDTable idColumnName='id_ferramenta' data={data as object[]} deleteFunction={remove} editFunction={edit} />
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