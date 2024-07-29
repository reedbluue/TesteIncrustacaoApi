import { BiSearch } from "react-icons/bi";
import { TbTrashFilled } from "react-icons/tb";
import { BiPencil } from "react-icons/bi";
import { useEffect, useState } from "react";
export const CRUDTable = ({ testePage, data, deleteFunction, editFunction, idColumnName }: { testePage?: boolean, data: object[], deleteFunction: (element: any) => void, editFunction: (element: any) => void, idColumnName: string }) => {
    const headers: Array<string> = data[0] ? Object.keys(data[0]) : [''];
    const [filteredData, setFilteredData] = useState(data);
    const [showingData, setShowingData] = useState(filteredData);
    const [qtdPages, setQtdPages] = useState(0);
    const [actualPage, setActualPages] = useState(0);

    // FILTRA A TABELA
    const filter = (value: string) => {
        if (value == "") {
            setFilteredData(data);
            return;
        }
        const newValue = data.filter(o =>
            Object.keys(o).some(k => {
                if (typeof (o[k as keyof object]) === 'string') {
                    return (o[k as keyof object] as string).toLowerCase().includes(value.toLowerCase());
                } else if (typeof (o[k as keyof object]) === 'number')
                    return o[k as keyof object] == value;
            }
            )
        )
        setActualPages(0);
        setFilteredData(newValue);
    }
    const nextPage = () => {
        if (actualPage < qtdPages) {
            setActualPages(actualPage + 1);
        }
    }
    const previewsPage = () => {
        if (actualPage > 0) {
            setActualPages(actualPage - 1);
        }
    }
    useEffect(() => {
        if (data.length > 0) {
            setFilteredData(data);
        }
    }, [data])
    useEffect(() => {
        if (data.length > 0) {
            setQtdPages(Math.floor(filteredData.length / 10));
            setShowingData(filteredData.slice(actualPage * 10, actualPage * 10 + 10));
        }
    }, [filteredData])
    useEffect(() => {
        setShowingData(filteredData.slice(actualPage * 10, actualPage * 10 + 10));
    }, [actualPage])

    return (
        <div className="mt-10 overflow-x-auto">
            <div className="relative w-full">
                <div className="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                    <BiSearch />
                </div>
                <input type="text" id="simple-search" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-bl-none rounded-br-none rounded-xl focus:ring-blue-500 focus:border-blue-500 block ps-10 p-2.5  dark:bg-gray-600 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Pesquisar" onChange={change => filter(change.target.value)} required />
            </div>
            {data.length > 0 ?
                <table className="table bg-gray-600 rounded-tl-none rounded-br-none">
                    {/* head */}
                    <thead>
                        <tr>
                            {testePage ?
                                <>
                                    <th className="text-lg font-bold">Excluir</th>
                                    <th className="text-lg font-bold">Editar</th>
                                </>:null
                            }
                            {headers?.map((item: any, index: any) => {
                                return (
                                    <th key={index} className="text-lg font-bold text-gray-400">{item}</th>
                                )
                            })}
                            {!testePage ?
                                <>
                                    <th className="text-lg font-bold">Excluir</th>
                                    <th className="text-lg font-bold">Editar</th>
                                </>:null
                            }
                        </tr>
                    </thead>
                    <tbody>
                        {showingData.map((row, index) => {
                            return (
                                <tr key={index} id={row[idColumnName as keyof object]} className=" hover:bg-gray-700 hover:text-black">
                                    {testePage ?
                                        <>
                                            <td><button className="btn btn-outline btn-sm" onClick={(element: any) => deleteFunction(element.target.parentNode.closest('tr').id)}><TbTrashFilled size={12} color="#ff5555" /></button></td>
                                            <td><button className="btn btn-outline btn-sm" onClick={(element: any) => editFunction(element.target.parentNode.closest('tr').id)}><BiPencil size={12} color="#ffff00" /></button></td>
                                        </>:null
                                    }
                                    {headers.map((item, index) => {
                                        return (
                                            <td key={index}>
                                                {row[item as keyof object]}
                                            </td>
                                        )
                                    })}
                                    {!testePage ?
                                        <>
                                            <td><button className="btn btn-outline btn-sm" onClick={(element: any) => deleteFunction(element.target.parentNode.closest('tr').id)}><TbTrashFilled size={12} color="#ff5555" /></button></td>
                                            <td><button className="btn btn-outline btn-sm" onClick={(element: any) => editFunction(element.target.parentNode.closest('tr').id)}><BiPencil size={12} color="#ffff00" /></button></td>
                                        </>:null
                                    }
                                </tr>);
                        })}
                    </tbody>
                </table>
                : null
            }
            <div className="flex justify-end ">
                <button onClick={previewsPage} className=" btn btn-ghost bg-gray-600 rounded-none rounded-bl-xl">«</button>
                <button className=" btn btn-ghost bg-gray-600 rounded-none">{actualPage}</button>
                <button onClick={nextPage} className=" btn btn-ghost bg-gray-600 rounded-none rounded-br-xl">»</button>
            </div>
        </div>
    )
}