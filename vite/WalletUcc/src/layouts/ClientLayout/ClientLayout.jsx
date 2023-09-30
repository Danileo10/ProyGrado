import { Navbar } from '../../components/Client'
import { FooterAdmin } from '../../components/Admin/FooterAdmin/FooterAdmin';
import './ClientLayout.scss';

export const ClientLayout = (props) => {
    const {children} = props;
  return (
    <>
      <div>
        <Navbar/>
       
      </div>

      
      <link rel="preconnect" href="https://fonts.googleapis.com"/>
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
      <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@600&family=Poppins:wght@300;500&display=swap" rel="stylesheet"/>
      {children} 
      <FooterAdmin/>
    </>
  )
}

