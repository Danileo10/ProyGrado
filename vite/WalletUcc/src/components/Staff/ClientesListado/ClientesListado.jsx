import { useEffect, useState } from 'react';

export const ClientesListado = () => {
    const [data, setData] = useState([]);
    const [clienteAEditar, setClienteAEditar] = useState(null); // Estado para el producto que se está editando
    const [nuevosDatos, setNuevosDatos] = useState({});
    

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('http://127.0.0.1:8000/api/ver_clientes/');
                if (!response.ok) {
                    throw new Error('No hay datos');
                }
                const jsonData = await response.json();
                setData(jsonData);
            } catch (error) {
                console.error('Error');
            }
        };
        fetchData();
    }, []);

    const handleEditar = (cliente) => {
        setClienteAEditar(cliente);
    };

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setNuevosDatos({ ...nuevosDatos, [name]: value });
    };

    const handleGuardarCambios = async () => {
        try {
            // Realizar la solicitud PATCH con los nuevos datos
            const response = await fetch(`http://127.0.0.1:8000/api/modificar_cliente/?id_cliente=${clienteAEditar.idcliente}`, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(nuevosDatos),
            });
    
            if (response.ok) {
                // Producto editado con éxito, puedes actualizar el estado o recargar la lista de productos
                console.log('Cliente editado con éxito');
                // Actualizar la lista de productos o realizar otras acciones necesarias
    
                // Realizar una nueva solicitud para obtener los datos actualizados
                const nuevaRespuesta = await fetch('http://127.0.0.1:8000/api/ver_clientes/');
                if (nuevaRespuesta.ok) {
                    const nuevosDatos = await nuevaRespuesta.json();
                    setData(nuevosDatos); // Actualizar el estado con los nuevos datos
                } else {
                    throw new Error('Error al obtener los datos actualizados');
                }
    
                setClienteAEditar(null); // Cerrar el formulario de edición
            } else {
                throw new Error('Error al editar el producto');
            }
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <>
            <h1>Listado de Clientes</h1>
            <ul>
                {data.map((item) => (
                    <li key={item.idcliente}>
                        <p>ID Cliente: {item.idcliente}</p>
                        <p>Nombre: {item.persona_idusuario.nombre}</p>
                        <p>Apellido: {item.persona_idusuario.apellido}</p>
                        <p>Email: {item.persona_idusuario.email}</p>
                        <p>Dirección: {item.direccion}</p>
                        {/* Agregar un enlace a la página de edición con el ID del cliente */}
                        <button onClick={() => handleEditar(item)}>Editar</button>
                    </li>
                ))}
            </ul>

            {clienteAEditar && (
                <div>
                    <h2>Editar Cliente</h2>
                    <form>
                        <input
                            type="text"
                            name="nombre"
                            value={nuevosDatos.nombre || clienteAEditar.persona_idusuario.nombre}
                            onChange={handleInputChange}
                            placeholder="Nombre"
                        />
                        <input
                            type="text"
                            name="nombre"
                            value={nuevosDatos.apellido || clienteAEditar.persona_idusuario.apellido}
                            onChange={handleInputChange}
                            placeholder="Nombre"
                        />
                        <input
                            type="text"
                            name="nombre"
                            value={nuevosDatos.email || clienteAEditar.persona_idusuario.email}
                            onChange={handleInputChange}
                            placeholder="Nombre"
                        />
                        <input
                            type="text"
                            name="nombre"
                            value={nuevosDatos.direccion || clienteAEditar.direccion}
                            onChange={handleInputChange}
                            placeholder="Nombre"
                        />
                        
                        <button type="button" onClick={handleGuardarCambios}>Guardar Cambios</button>
                    </form>
                </div>
            )}
        </>
    );
};
