import './RegisterAdmin.scss';
import { RegisterForm } from '../../../components/Admin/RegisterForm';
import logo from '../../../../public/logofa.png';

export const RegisterAdmin = () => {
  return (
    <>
      <div className='register-admin'>
        <div className='register-admin__content'>
            <h1>Fieles Angelitos</h1>
            <img className='logo' src={logo} alt="Logo" />
            <RegisterForm/>
        </div>
      </div>
    </>
  )
}


