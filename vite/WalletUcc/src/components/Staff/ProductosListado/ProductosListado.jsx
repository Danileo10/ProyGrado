import { useEffect, useState } from 'react';

export const ProductosListado = () => {
    const [data, setData] = useState([]);
    const [productoAEditar, setProductoAEditar] = useState(null); // Estado para el producto que se está editando
    const [nuevosDatos, setNuevosDatos] = useState({}); // Estado para los nuevos datos del producto

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('http://127.0.0.1:8000/api-comercio/mostrar_producto');
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

    // Función para manejar el clic en el botón "Editar"
    const handleEditar = (producto) => {
        setProductoAEditar(producto);
    };

    // Función para manejar los cambios en los campos de edición
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setNuevosDatos({ ...nuevosDatos, [name]: value });
    };

    // Función para enviar la solicitud PATCH al servidor
    // Función para enviar la solicitud PATCH al servidor
const handleGuardarCambios = async () => {
    try {
        // Realizar la solicitud PATCH con los nuevos datos
        const response = await fetch(`http://127.0.0.1:8000/api-comercio/modificar_producto/?id_producto=${productoAEditar.idproducto}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(nuevosDatos),
        });

        if (response.ok) {
            // Producto editado con éxito, puedes actualizar el estado o recargar la lista de productos
            console.log('Producto editado con éxito');
            // Actualizar la lista de productos o realizar otras acciones necesarias

            // Realizar una nueva solicitud para obtener los datos actualizados
            const nuevaRespuesta = await fetch('http://127.0.0.1:8000/api-comercio/mostrar_producto');
            if (nuevaRespuesta.ok) {
                const nuevosDatos = await nuevaRespuesta.json();
                setData(nuevosDatos); // Actualizar el estado con los nuevos datos
            } else {
                throw new Error('Error al obtener los datos actualizados');
            }

            setProductoAEditar(null); // Cerrar el formulario de edición
        } else {
            throw new Error('Error al editar el producto');
        }
    } catch (error) {
        console.error(error);
    }
};


    return (
        <>
            <h1>Listado de Productos</h1>
            <ul>
                {data.map((item) => (
                    <li key={item.idproducto}>
                        <p>{item.nombre}</p>
                        <p>{item.precio}</p>
                        <p>{item.descripcion}</p>
                        <p>{item.imagen}</p>
                        <button onClick={() => handleEditar(item)}>Editar</button>
                    </li>
                ))}
            </ul>

            {productoAEditar && (
                <div>
                    <h2>Editar Producto</h2>
                    <form>
                        <input
                            type="text"
                            name="nombre"
                            value={nuevosDatos.nombre || productoAEditar.nombre}
                            onChange={handleInputChange}
                            placeholder="Nombre"
                        />
                        <input
                            type="text"
                            name="precio"
                            value={nuevosDatos.precio || productoAEditar.precio}
                            onChange={handleInputChange}
                            placeholder="Precio"
                        />
                        <input
                            type="text"
                            name="descripcion"
                            value={nuevosDatos.descripcion || productoAEditar.descripcion}
                            onChange={handleInputChange}
                            placeholder="Descripción"
                        />
                        <input
                            type="text"
                            name="imagen"
                            value={nuevosDatos.imagen || productoAEditar.imagen}
                            onChange={handleInputChange}
                            placeholder="Imagen"
                        />
                        <button type="button" onClick={handleGuardarCambios}>Guardar Cambios</button>
                    </form>
                </div>
            )}
        </>
    );
};
