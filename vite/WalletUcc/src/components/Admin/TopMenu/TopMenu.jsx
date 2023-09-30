import './TopMenu.scss';
import { Icon, Menu } from 'semantic-ui-react'
import { useAuth } from '../../../hooks'
import { Link } from 'react-router-dom';

export const TopMenu = () => {
  const { auth, logout } = useAuth();

  const renderName = () => {
    if (auth.me?.nombre && auth.me?.apellido) {
      return `${auth.me?.nombre} ${auth.me.apellido}`
    }

    return auth.me?.email
  }
  return (
    <>
      <Menu fixed='top' className='top-menu-admin'>
        <Menu.Item className='top-menu-admin__logo'>
          <p>Fieles Angelitos</p>
        </Menu.Item>
        {auth.me.is_staff &&
          <Menu.Item>
            <Link to={"/staff/clientes"}>
              clientes Admin
            </Link>
          </Menu.Item>
        }
        {auth.me.is_staff &&
          <Menu.Item>
            <Link to={"/staff/productos"}>
              productos Admin
            </Link>
          </Menu.Item>
        }
        {auth.me.is_staff &&
          <Menu.Item>
            <Link to={"/staff/pedidos"}>
              pedidos Admin
            </Link>
          </Menu.Item>
        }
        {auth.me.is_staff &&
          <Menu.Item>
            <Link to={"/staff/citas"}>
              citas Admin
            </Link>
          </Menu.Item>
        }

        <Menu.Item>
          <Link to={"/admin/mascotas"}>
            MASCOTAS
          </Link>
        </Menu.Item>

        <Menu.Item>
          <Link to={"/admin/productos"}>
            productos
          </Link>
        </Menu.Item>

        <Menu.Item>
          <Link to={"/admin/citas"}>
            citas
          </Link>
        </Menu.Item>

        <Menu.Menu position='right'>
          <Menu.Item>Hola, {renderName()}</Menu.Item>
          <Menu.Item onClick={logout}>
            <Icon name='sign-out'></Icon>
          </Menu.Item>
          <Menu.Item>
            <Link to={"/admin/perfil"}>
              perfil
            </Link>
          </Menu.Item>
          <Menu.Item>
            <Link to={"/admin/carrito "}>
              🛒
            </Link>
          </Menu.Item>

        </Menu.Menu>
      </Menu>
    </>
  )
}

export default TopMenu
