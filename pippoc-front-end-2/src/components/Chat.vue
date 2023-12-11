<template>
    <v-card title="Salida de Chat" variant="tonal">
        <v-card-text v-if="res">
            {{ res.data.content }}
        </v-card-text>
        <v-text-field label="¿Que deseas de la IA?" variant="solo-inverted" v-model="mensaje"></v-text-field>
        <v-card-actions>
            <v-btn @click="submit" :loading="loading_timer" :disabled="loading_timer"> <v-icon>mdi-send</v-icon>  Enviar</v-btn>
        </v-card-actions>
    </v-card>  
</template>


<script>
import axios from 'axios';

export default{
    data(){   
        return{
            loading_timer: false,
            res:null,
            mensaje:null
        }
    },
    methods:{
        async submit(){
            try{
                this.loading_timer = true
                await axios.post("http://127.0.0.1:8000/api/gpt_request/", this.mensaje)
                .then( response =>{
                    this.res = response
                    this.loading_timer = false
                    }
                )
            }
            catch (error){
                console.log(error)
            }
        }
    }
}
</script>