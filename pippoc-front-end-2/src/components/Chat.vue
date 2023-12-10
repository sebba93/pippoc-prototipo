<template>
    <v-card title="Salida de Chat" variant="tonal">
        <v-card-text v-if="res">
            {{ res.data.content }}
        </v-card-text>
        <v-text-field label="¿Que deseas de la IA?" variant="solo-inverted" v-model="mensaje"></v-text-field>
        <v-card-actions>
            <v-btn @click="submit"> <v-icon>mdi-send</v-icon>  Enviar</v-btn>
        </v-card-actions>
    </v-card>  
</template>


<script>
import axios from 'axios';

export default{
    data(){   
        return{
            res:null,
            mensaje:null
        }
    },
    methods:{
        async submit(){
            this.res = await axios.post("http://127.0.0.1:8000/api/gpt_request/", this.mensaje)
            if (this.res.data == null) {
                return{
                    res: null,
                    mensaje: null
                }
            }
            else {
                return{
                    res:this.res.data,
                    mensaje: null
                }
            }
        }
    }
}
</script>