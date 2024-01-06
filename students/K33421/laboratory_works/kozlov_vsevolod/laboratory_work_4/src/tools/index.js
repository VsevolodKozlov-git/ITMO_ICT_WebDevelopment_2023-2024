import axios from "axios";

export async function fetchData(url, filename, config={}){
    try{
        const response = await axios.get(url, config)
        return response.data
    }
    catch (e) {
        throw new Error(`api get error in file: ${filename}\n url:${url}`);
    }
}

export async function postData(url, filename, data){
    try{
        const response = await axios.post(url, data)
        return response.data
    }
    catch (e) {
        throw new Error(`api post error in file: ${filename}\n url:${url}`);
    }
}

export async function deleteData(url, filename){
    try{
        const response = await axios.delete(url)
        return response.data
    }
    catch (e) {
        throw new Error(`api delete error in file: ${filename}\n url:${url}`);
    }
}