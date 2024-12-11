<template>
  <div>
    <h1>Cotizador de Impresión 3D</h1>
    <form @submit.prevent="cotizar">
      <label>Largo del modelo (cm):</label>
      <input type="number" v-model="form.largo" required />

      <label>Ancho del modelo (cm):</label>
      <input type="number" v-model="form.ancho" required />

      <label>Alto del modelo (cm):</label>
      <input type="number" v-model="form.alto" required />

      <label>Densidad de infill (%):</label>
      <input type="number" v-model="form.densidad_infill" required />

      <label>Velocidad de impresión (mm/s):</label>
      <input type="number" v-model="form.velocidad_impresion" required />

      <label>Tipo de filamento:</label>
      <select v-model="form.tipo_filamento" required>
        <option value="pla">PLA</option>
        <option value="ptge">PTGE</option>
        <option value="abs">ABS</option>
        <option value="tpu">TPU</option>
      </select>

      <label>¿Requiere acabados?</label>
      <select v-model="form.acabados" required>
        <option value="true">Sí</option>
        <option value="false">No</option>
      </select>

      <label>Tiempo de impresión (horas):</label>
      <input type="number" v-model="form.tiempo_impresion" required />

      <label>Peso del modelo (g):</label>
      <input type="number" v-model="form.peso_modelo" required />

      <label>Filamento consumido (metros):</label>
      <input type="number" v-model="form.filamento_consumido" required />

      <label>Costo de envío:</label>
      <input type="number" v-model="form.costo_envio" required />

      <button type="submit">Calcular Cotización</button>
    </form>

    <div v-if="cotizacion">
      <h2>Resultado de la Cotización</h2>
      <pre>{{ cotizacion }}</pre>
      <button @click="guardarPedido">Confirmar Pedido</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { createClient } from "@supabase/supabase-js";

const supabase = createClient("https://tu-supabase-url.supabase.co", "tu-clave-publica");

export default {
  data() {
    return {
      form: {
        largo: "",
        ancho: "",
        alto: "",
        densidad_infill: "",
        velocidad_impresion: "",
        tipo_filamento: "pla",
        acabados: "false",
        tiempo_impresion: "",
        peso_modelo: "",
        filamento_consumido: "",
        costo_envio: "",
      },
      cotizacion: null,
    };
  },
  methods: {
    async cotizar() {
      try {
        const response = await axios.post("http://localhost:5000/cotizar", this.form);
        this.cotizacion = response.data;
      } catch (error) {
        console.error("Error al calcular la cotización:", error);
      }
    },
    async guardarPedido() {
      try {
        const { error } = await supabase.from("pedidos").insert([{ ...this.form, total: this.cotizacion.total }]);
        if (error) throw error;
        alert("Pedido guardado exitosamente.");
      } catch (error) {
        console.error("Error al guardar el pedido:", error);
        alert("No se pudo guardar el pedido.");
      }
    },
  },
};
</script>

<style>
form {
  display: flex;
  flex-direction: column;
  max-width: 400px;
}
label {
  margin-top: 10px;
}
button {
  margin-top: 20px;
}
</style>
