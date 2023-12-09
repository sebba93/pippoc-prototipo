<template>
    <v-card variant="ourlined">
        <v-tabs
            v-model="tab"
            bg-color="indigo"
        >
            <v-tab value="one">Unidad 1</v-tab>
            <v-tab value="two">Unidad 2</v-tab>
            <v-tab value="three">Unidad 3</v-tab>
        </v-tabs>
    
        <v-card-text>
            <v-window v-model="tab">
            <v-window-item value="one">
                <v-card variant="outlined">
                    <h2>Sección 1</h2>
                    <v-checkbox color="indigo">
                        <template v-slot:label><div>
                            <h3><v-icon>mdi-file</v-icon> 1.1 Lectura - El Peligro en el Trabajao</h3>
                        </div></template>
                    </v-checkbox>

                    <v-checkbox color="indigo">
                        <template v-slot:label><div>
                            <h3><v-icon>mdi-gesture-tap-box</v-icon> 1.2 Actividad - Recordando Conceptos </h3>
                        </div></template>
                    </v-checkbox>

                    <v-checkbox color="indigo">
                        <template v-slot:label><div>
                            <h3><v-icon>mdi-video-vintage</v-icon> 1.3 Video - Accidentes Reales</h3>
                        </div></template>
                    </v-checkbox>

                    
                    <v-btn> Agregar Elemento a Sección</v-btn>
                </v-card>

                <v-divider></v-divider>

                <v-card variant="outlined">
                    <h2>Sección 2</h2>
                    <v-checkbox color="indigo">
                        <template v-slot:label><div>
                            <h3><v-icon>mdi-note-edit</v-icon> Prueba 1: El Peligro en el Trabajao </h3>
                        </div></template>
                    </v-checkbox>
                </v-card>
            </v-window-item>
  
            <v-window-item value="two">
                <v-card variant="outlined">
                        <h2>Anexos</h2>
                        <v-checkbox color="indigo">
                            <template v-slot:label>
                                <div>
                                    <h3><v-icon>mdi-folder</v-icon> 2.1 Investiga - Carpeta de Documentos </h3>
                                </div>
                            </template>
                        </v-checkbox>
                    </v-card> 
            </v-window-item>
    
            <v-window-item value="three">
                <v-card variant="outlined">
                        <h2>Anexos</h2>
                        <v-checkbox color="indigo">
                            <template v-slot:label>
                                <div>
                                    <h3><v-icon>mdi-file-pdf-box</v-icon> 3.1 Leamos - Investigación de Campo </h3>
                                </div>
                            </template>
                        </v-checkbox>
                    </v-card> 
            </v-window-item>

            </v-window>
        </v-card-text>


      


    </v-card>
  </template>
  
<script>
import { getDocumentos } from '@/axios/documentosAxios';

export default {
  data() {
    return {
      documentos: [],
      tab: null, // Add a tab property for v-model
    };
  },
  mounted() {
    // Fetch documentos from Django backend using the imported function
    getDocumentos()
      .then(data => {
        this.documentos = data;
        // Do any additional processing with documentos if needed
      })
      .catch(error => {
        // Handle error if needed
      });
  },
  // Other methods and component logic
};
</script>
