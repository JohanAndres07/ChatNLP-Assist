
const url = 'http://127.0.0.1:3000/messages';

export const messages = async ()=> {

    try{
        const response = await fetch(url);
        const data = await response.json();
        // console.log(data.chat.messages);
        return(data.chat.messages);
    }catch(err){
        console.error("err",err);
    }

}