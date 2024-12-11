<template>
  <div id="app">
    <CotizadorPrincipal />
  </div>
</template>

<script>
import CotizadorPrincipal from "./components/CotizadorPrincipal.vue";

export default {
  name: "App",
  components: {
    CotizadorPrincipal,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
