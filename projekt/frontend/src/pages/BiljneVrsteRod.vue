<template>
  <q-page>
    <h1>Biljna vrsta - test</h1>
    <div>{{ message.hrvatski_naziv_vrste }}</div>
    <div>{{ message.latinski_naziv }}</div>
    <div>{{ message.sinonim_vrste }}</div>
    <div>{{ message.opis_vrste }}</div>
    <div>{{ message.ID_roda }}</div>
  </q-page>
</template>
<style>
</style>
<script>
export default {
  name: 'PageIndex',
  data () {
    return {
      message: 'xxx'
    }
  },
  created () {
    this.$axios.get('http://193.198.97.14:8000/api/biljnevrste/2/?format=json')
      .then(response => {
        this.message = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>
