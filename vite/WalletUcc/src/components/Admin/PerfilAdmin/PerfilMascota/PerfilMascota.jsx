import { useEffect, useState } from "react";
import { useAuth } from "../../../../hooks";



export const PerfilMascota = () => {
    const [mascotas, setMascotas] = useState([]);
    const { auth } = useAuth();
    useEffect(() => {
        const fetchData = async () => {
            try {

                console.log(auth)
                const response = await fetch(`http://127.0.0.1:8000/api/mascota_esp/?id_cliente=${auth.me.idcliente}`);
                if (!response.ok) {
                    throw new Error('No hay datos');
                }
                const jsonData = await response.json();
                setMascotas(jsonData);
                console.log(jsonData)
            } catch (error) {
                console.error('Error');
            }
        };
        fetchData();
    }, []);
    return (
        <>
           <h1>Mascotas</h1>
            <ul>
                {mascotas.map((mascota) => (
                    <li key={mascota.idmascota}>
                        <p>Nombre: {mascota.nombre}</p>
                        <p>Fecha de nacimiento: {mascota.fecha_nacim}</p>
                        <p>Raza: {mascota.raza}</p>
                        <p>Fecha de defunción: {mascota.fecha_defun}</p>
                        {/* Agrega aquí otras propiedades de la mascota que desees mostrar */}
                    </li>
                ))}
            </ul>

        </>
    )
}


