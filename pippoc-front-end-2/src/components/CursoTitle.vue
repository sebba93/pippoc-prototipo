<template>
    <v-card
    :title="descripcion"
    :subtitle="categoria"
    text="Curso de Prevención de Riesgos diseñada para la minera 'Pueblo Minera'"
    variant="outlined"
    prepend-icon="mdi-home"
    >
        <v-card-actions>
            <v-lists>
                <h1 class="ma-1"><v-icon>mdi-file-outline</v-icon> Reglamento del Curso </h1>
                <h1 class="ma-1"><v-icon>mdi-folder</v-icon> Carpeta Genera del Curso </h1>
                <h1 class="ma-1"><v-icon>mdi-file-outline</v-icon> Planificación General del Curso </h1>
            </v-lists>

        </v-card-actions>
    </v-card>
    <v-divider></v-divider>
</template>

<script>
  import { getCursos } from '../axios/cursosAxios';
  import { getParticipantes } from '../axios/participantesAxios';
  
  export default {
    data() {
      return {
        descripcion: null,
        categoria: null
        //cursos: [],
        //participantes: [],
      };
    },
    mounted() {
      // Fetch cursos from Django backend using the imported function
      getCursos()
        .then(response => {
          this.descripcion = response[0].descripcion;
          this.categoria = response[0].categoria;
          // After fetching cursos, fetch participantes
          return getParticipantes();
        })
        .then(data => {
          this.participantes = data;
        })
        .catch(error => {
          // Handle error if needed
        });
    },
    // Other methods and component logic
  };
  </script>
  