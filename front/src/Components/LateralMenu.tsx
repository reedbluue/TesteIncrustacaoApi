import { Link } from "react-router-dom"

export const LateralMenu = () => {

    return (
        <div className='h-full bg-[#D9D9D9] self-center w-1/3 mb-4 lg:mb-0 lg:w-1/6 items-center mr-5 rounded-3xl'>
            <ul className="menu menu-vertical ">
                <li>
                    <Link to={"/CreateTest"} className="text-black text-sm xl:text-xl  my-1 btn btn-ghost h-full w-full lg:mt-20 p-3 flex-col">
                        Criar Teste

                    </Link>
                </li>
                <li>
                    <details >
                        <summary className="text-black text-sm xl:text-xl  my-1 btn btn-ghost h-full w-full lg:mt-20 p-3">Parametrização</summary>
                        <ul>
                            <li ><Link to={'/AnaliseMev'} className="text-black text-xs md:text-base my-1 p-3">Análise Mev</Link></li>
                            <li ><Link to={'/FerramentaUS'} className="text-black text-xs md:text-base my-1 p-3">FerramentaUS</Link></li>
                            <li ><Link to={'/MetodoIncrustacao'} className="text-black text-xs md:text-base my-1 p-3">Método Incrustração</Link></li>
                            <li ><Link to={'/MetodoPrecipitacao'} className="text-black text-xs md:text-base my-1 p-3">Método Precipitação</Link></li>
                            <li ><Link to={'/Reagente'} className="text-black text-xs md:text-base my-1 p-3">Reagente</Link></li>
                            <li ><Link to={'/SolucaoIncrustante'} className="text-black text-xs md:text-base my-1 p-3">Solução Incrustante</Link></li>
                            <li ><Link to={'/SolucaoLimpeza'} className="text-black text-xs  md:text-base my-1 p-3">Solução Limpeza</Link></li>
                            {/* <li ><Link to={'/SolucaoReagente'} className="text-black text-xs md:text-base my-1 p-3">Solução Reagente</Link></li> */}
                        </ul>
                    </details>
                </li>
            </ul>
        </div>
    )
}