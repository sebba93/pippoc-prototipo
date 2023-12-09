import axios from "axios";

export const getDocumentos = () => {
    return axios
        .get('http://127.0.0.1:8000/documentos/')
        .then(response => {
            return response.data;
        })
        .catch(error => {
            console.error('Error getting documentos:', error);
            throw error;
        });
}

export const downloadDocumento = (id) => {
    return axios
        .get(`http://127.0.0.1:8000/documentos/${id}`)
        .then(response => {
            return response.data;
        })
        .catch(error => {
            console.error('Error getting documento:', error);
            throw error;
        });
}

export const uploadDocumento = (documento,data) => {
    return axios
        .post('http://127.0.0.1:8000/documentos/',documento,data)
        .then(response => {
            return response.data;
        })
        .catch(error => {
            console.error('Error uploading documento:', error);
            throw error;
        });
}
