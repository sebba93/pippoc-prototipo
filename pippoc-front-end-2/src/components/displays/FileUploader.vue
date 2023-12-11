<template>
    <v-dialog>
        <div justify="center" align="center">
            <v-card title="Agregar elemento" max-height="500" max-width="800">
                <div class="ma-5">    
                    <v-text-field label="Nombre del elemento" v-model="nombre"></v-text-field>
                    <v-file-input label="Suba su archivo" accept=".pdf" v-model="archivo"></v-file-input>
                    <v-btn @click ="upload" :loading="loading_timer" :disabled="loading_timer"> 
                        Subir
                    </v-btn>
                </div>
            </v-card>
        </div>
    </v-dialog>
</template>

<script>
import axios from 'axios';

export default{
    data(){   
        return{
            loading_timer: false,
            nombre:null,
            archivo:null
        }
    },
    methods:{
        async upload(){
            this.loading_timer = true
            let formData = new FormData()
            formData.append("archivo", this.archivo['0'])
            await axios.post("http://127.0.0.1:8000/api/upload/", formData, {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            }).then( response =>{
                this.loading_timer = false
                }
            )
            /*this.archivo = await axios.post("http://127.0.0.1:8000/api/upload/", this.archivo)
            .then( response =>{
                console.log(response)
                this.loading_timer = false
                }
            )*/       
        }
    }
}
</script>