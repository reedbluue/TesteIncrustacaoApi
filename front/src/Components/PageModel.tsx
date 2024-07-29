import { Footer } from "./Footer"
import { HeaderMenu } from "./HeaderMenu"

export const PageModel = ({ children }: { children?: any }) => {
    return (
        //modelo de página contendo footer e header pré setados com o espaço para conteudo
        <div className="flex flex-col justify-between h-screen">
            <HeaderMenu />
            <div className=" mt-2 mx-12 p-4">
                {children}
            </div>
            <Footer />
        </div>
    )
}