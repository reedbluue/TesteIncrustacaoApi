import { BrowserRouter, Route, Routes } from "react-router-dom";
import { HomePage } from "../Pages/HomePage";
import { CreateTest } from "../Pages/CreateFlux/CreateTest";
import { MetodoIncrustacao } from "../Pages/Parametrizacao/MetodoIncrustacao";
import { SolucaoLimpeza } from "../Pages/Parametrizacao/SolucaoLimpeza";
import { MetodoPrecipitacao } from "../Pages/Parametrizacao/MetodoPrecipitacao";
import { Reagente } from "../Pages/Parametrizacao/Reagente";
import { SolucaoIncrustante } from "../Pages/Parametrizacao/SolucaoIncrustante";
import { FerramentaUS } from "../Pages/Parametrizacao/FerramentaUS";
// import { SolucaoReagente } from "../Pages/Parametrizacao/SolucaoReagente";
import { AnaliseMev } from "../Pages/Parametrizacao/AnaliseMev";
export const AppRoutes = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" Component={HomePage} />
                <Route path="/CreateTest" Component={CreateTest} />
                <Route path="/MetodoIncrustacao" Component={MetodoIncrustacao} />
                <Route path="/SolucaoLimpeza" Component={SolucaoLimpeza} />
                <Route path="/MetodoPrecipitacao" Component={MetodoPrecipitacao} />
                <Route path="/Reagente" Component={Reagente} />
                <Route path="/SolucaoIncrustante" Component={SolucaoIncrustante} />
                <Route path="/FerramentaUS" Component={FerramentaUS} />
                {/* <Route path="/SolucaoReagente" Component={SolucaoReagente} /> */}
                <Route path="/AnaliseMev" Component={AnaliseMev} />
            </Routes>
        </BrowserRouter>
    )
}