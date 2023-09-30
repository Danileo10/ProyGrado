import { useAuth } from '../../../../hooks'

export const PerfilUsuario = () => {
  const {auth} = useAuth();
  console.log(auth)
  
  return (
    <>
    
      <h1>Perfil</h1>
      <p>{auth.me.nombre}</p>
      <p>{auth.me.apellido}</p>
      <p>{auth.me.email}</p>
      <p>{auth.me.telefono}</p>
      <p>{auth.me.direccion}</p>
      
    </>
  )
}

