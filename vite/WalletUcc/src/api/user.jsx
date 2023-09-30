import { ErrorMessage } from "formik";
import { BASE_API } from "../utils/constants";

export const loginApi = async(formValue) => {
    //eslint-disable-next-line
    try{
        const url = `${BASE_API}/token/`;
        const params = {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formValue),
        };

        const response = await fetch(url, params);

        if(response.status !== 200){
            throw new Error("ususario o contraseña incorrecto");
        }

        const result = await response.json();

        return result;
    }catch(error){
        throw error;
    }
}

export const crearMascotaApi = async(formValue, id) => {
    //eslint-disable-next-line
    try{
        const url = `${BASE_API}/api/mascota_crear/?id_cliente=${id}`;
        const params = {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formValue),
        };

        const response = await fetch(url, params);

        if(response.status !== 200){
            throw new Error(response.statusText);
        }

        const result = await response.json();

        return result;
    }catch(error){
        throw error;
    }
}

export const crearCitaApi = async(formValue) => {
    //eslint-disable-next-line
    try{
        const url = `${BASE_API}/api-citas/guardar_cita/`;
        const params = {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formValue),
        };

        console.log(JSON.stringify(formValue))

        const response = await fetch(url, params);

        if(response.status !== 200){
            throw new Error(response.statusText);
        }

        const result = await response.json();

        return result;
    }catch(error){
        throw error;
    }
}

export const crearProductoApi = async(formValue) => {
    //eslint-disable-next-line
    try{
        const url = `${BASE_API}/api-comercio/crear_producto/`;
        const params = {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formValue),
        };

        const response = await fetch(url, params);

        if(response.status !== 200){
            throw new Error(response.statusText);
        }

        const result = await response.json();

        return result;
    }catch(error){
        throw error;
    }
}

export const modificarProductoApi = async(formValue, id_producto) => {
    //eslint-disable-next-line
    try{
        const url = `${BASE_API}/api-comercio/crear_producto/`;
        const params = {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formValue),
        };

        const response = await fetch(url, params);

        if(response.status !== 200){
            throw new Error(response.statusText);
        }

        const result = await response.json();

        return result;
    }catch(error){
        throw error;
    }
}




export const registerApi = async(formValue) => {
    //eslint-disable-next-line
    try{
        const url = `${BASE_API}/api/guardar_cliente/`
        const params = {
            method: 'POST',
            headers: { 
                'Content-Type': "application/json",
            },
            body: JSON.stringify(formValue),};  
            
        const response = await fetch(url, params);
        
        if(response.status !== 200){
            throw new Error(response.statusText)
        }

        const result = await response.json();
        return result
    }catch(error){
        throw error;
    }
}


export const getMeApi = async(token) => {
    //eslint-disable-next-line
    try{
        const url = `${BASE_API}/api/auth/`;
        const params = {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        };

        const response = await fetch(url, params);
        const result = await response.json();
        return result
    }catch(error){
        throw error;
    }
}

