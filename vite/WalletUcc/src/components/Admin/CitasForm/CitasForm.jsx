import { useEffect, useState } from "react";


import { Form, Button } from 'semantic-ui-react';

import { useFormik } from 'formik';
import * as Yup from 'yup'
import { useAuth } from '../../../hooks'

import { crearCitaApi } from '../../../api/user'


export const CitasForm = () => {
    //console.log(useAuth())
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

    const bloquesOptions = [
        { key: '1', text: '8-9', value: 1 },
        { key: '2', text: '9-10', value: 2 },
        { key: '3', text: '10-11', value: 3 },
        { key: '4', text: '11-12', value: 4 },
        { key: '5', text: '2-3', value: 5 },
        { key: '6', text: '3-4', value: 6 },
        { key: '7', text: '4-5', value: 7 },
        { key: '8', text: '5-6', value: 8 },
        { key: '9', text: '6-7', value: 9 },
        { key: '10', text: '7-8', value: 10 },
    ]

    const serviciosOptions = [
        { key: '1', text: 'Baño', value: 1 },
        { key: '2', text: 'Revisión general', value: 2 },
        { key: '3', text: 'Peluquería', value: 3 },
        { key: '4', text: 'Vacunación', value: 4 },
    ]

    const mascotasOptions = mascotas.map((mascota, index) =>{
        return{
            key: index, text: `${mascota.nombre} - ${mascota.raza}`, value: mascota.idmascota
        }
    })


    const formik = useFormik({
        initialValues: initialValues(auth.me.idcliente),
        validationSchema: Yup.object(validationSchema()),
        onSubmit: async (formValue) => {
            try {
                console.log(formValue)
                const response = await crearCitaApi(formValue);
                console.log(response)

            } catch (e) {
                console.log("Error");
                console.log(e);
            }
        }
    });



    return (
        <>
            <Form className='login-form-admin' onSubmit={formik.handleSubmit}>
                <Form.Input
                    name="fecha"
                    type='date'
                    placeholder="Fecha de la cita"
                    value={formik.values.text}
                    onChange={formik.handleChange}
                    error={formik.errors.string}
                />
                <Form.Select
                    name="id_bloque"
                    options={bloquesOptions}
                    placeholder="Bloque de horas"
                    value={formik.values.text}
                    onChange={(e, { value }) => formik.setFieldValue("id_bloque", value)}
                    error={formik.errors.id_bloque}
                />
                <Form.Select
                    name="id_servicio"
                    options={serviciosOptions}
                    placeholder="Servicio"
                    value={formik.values.text}
                    onChange={(e, { value }) => formik.setFieldValue("id_servicio", value)}
                    error={formik.errors.id_servicio}
                />
                <Form.Select
                    name="id_mascota"
                    options={mascotasOptions}
                    placeholder="mascotas"
                    value={formik.values.text}
                    onChange={(e, { value }) => formik.setFieldValue("id_mascota", value)}
                    error={formik.errors.id_servicio}
                />
                <div className='contenedorBtn'>
                    <Button type='submit' content="Crear" primary fluid />

                </div>

            </Form>
        </>
    )
}

const initialValues = (id) => {
    return {
        id_cliente: id,
        fecha: "",
        id_bloque: "",
        id_servicio: "",
        id_mascota: "",
    };
}

const validationSchema = () => {
    return {

    }
}