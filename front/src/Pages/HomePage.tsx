import { LateralMenu } from '../Components/LateralMenu'
import { PageModel } from '../Components/PageModel'
import UfbaLogo from '../assets/UfbaLogo.png'
import { Link } from 'react-router-dom'
export const HomePage = () => {

    return (
        <div>
            {/* modelo de página */}
            <PageModel>
                {/* Menu Horizontal */}
                <div className=' flex flex-col h-full lg:flex-row md:justify-center'>
                   <LateralMenu/>
                    {/* Read Me lateral para informações necessárias */}
                    <div className='h-full bg-[#D9D9D9] w-full lg:w-5/6 rounded-3xl p-20 relative'>
                        <div className='mb-14'>
                            <p className='text-black text-6xl mb-2'>Sobre:</p>
                            <div className='flex justify-end'>
                                <p className='text-black w-[90%] justify-end text-justify indent-14 text-xl'>
                                    Lorem ipsum blandit condimentum felis lectus est nostra, laoreet himenaeos dapibus fringilla gravida tempus per donec, curae aliquam risus libero ut mattis. suspendisse posuere faucibus tempus duis donec proin nec curabitur eu facilisis at, scelerisque felis vehicula condimentum sit lacus amet ad commodo dapibus, eu neque habitasse elementum pharetra porttitor erat sapien conubia ac. nec congue enim etiam praesent turpis nisl elementum, sollicitudin purus praesent ligula volutpat proin, duis proin commodo primis mollis suspendisse. volutpat imperdiet sociosqu leo sociosqu condimentum, cursus dictumst sed torquent porttitor primis, platea ligula ut enim.
                                </p>
                            </div>
                        </div>
                        <div>
                            <p className='text-black text-6xl mb-2'>Objetivo:</p>
                            <div className='flex justify-end'>
                                <p className='text-black w-[90%] justify-end text-justify indent-14 text-xl'>
                                    Lorem ipsum blandit condimentum felis lectus est nostra, laoreet himenaeos dapibus fringilla gravida tempus per donec, curae aliquam risus libero ut mattis. suspendisse posuere faucibus tempus duis donec proin nec curabitur eu facilisis at, scelerisque felis vehicula condimentum sit lacus amet ad commodo dapibus, eu neque habitasse elementum pharetra porttitor erat sapien conubia ac. nec congue enim etiam praesent turpis nisl elementum, sollicitudin purus praesent ligula volutpat proin, duis proin commodo primis mollis suspendisse. volutpat imperdiet sociosqu leo sociosqu condimentum, cursus dictumst sed torquent porttitor primis, platea ligula ut enim.
                                </p>
                            </div>
                        </div>
                        <img src={UfbaLogo} className='absolute m-auto left-0 right-0 top-0 bottom-0 ' />
                    </div>
                </div>
            </PageModel>
        </div>
    )
}