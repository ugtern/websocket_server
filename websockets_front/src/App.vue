<template>
  <div id="app">
    <div class="center">

    </div>
    <div class="right_panel">
      <Home/>
    </div>
  </div>
</template>

<script>
import Home from "./components/home";

export default {
  name: 'app',
  components: {
    Home
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
    display: flex;
}
#app input {
  display: flex;
}
    .center {
        flex-grow: 1;
    }
</style>
