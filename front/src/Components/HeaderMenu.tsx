import { Link } from "react-router-dom"

export const HeaderMenu = () => {
    return (
        <div className="bg-[#D9D9D9] flex-none">
            <div className="flex justify-between">
                <div className="flex items-center">
                    <Link to={"/"} className="text-black md:text-xl my-1 btn btn-ghost w-full">Teste Incrustação Carbonatica</Link>
                </div>
                <div>
                    <ul className="menu menu-horizontal justify-center sm:justify-end px-1">
                        <li><button className="text-black md:text-md my-1 btn btn-ghost" onClick={()=>alert("click")}>Criar Teste</button></li>
                        <li><button className="text-black md:text-md my-1 btn btn-ghost" onClick={()=>alert("click")}>Listar Testes</button></li>
                        <li><button className="text-black md:text-md my-1 btn btn-ghost" onClick={()=>alert("click")}>Iniciar Teste</button></li>
                        <li><button className="text-black md:text-md my-1 btn btn-ghost" onClick={()=>alert("click")}>Resultados</button></li>
                    </ul>
                </div>
            </div>
        </div>
    )
}