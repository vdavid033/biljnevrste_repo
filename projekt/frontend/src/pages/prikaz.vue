<template>
 <q-page padding="">
<div>
Hrvatski naziv: {{ vrsta.hrvatski_naziv_vrste }} &emsp; &emsp; &emsp; &nbsp;
Sinonim: {{ vrsta.sinonim_vrste }}
  </div>
  <div></div>
  <div>
Latinski naziv:
  </div>
   <div>&nbsp;</div>
    <div>
Varijet:
  </div>
   <div>&nbsp;</div>
    <div>
Uporabni dio: &emsp; &emsp; &emsp; &emsp; Bioaktivna tvar:
  </div>
   <div>&nbsp;</div>
    <div>
OPIS BILJKE:
  </div>
  <div>
    <div class="layout-padding">
      {{ vrsta.opis_vrste }}
    </div>
  </div>
  <div class="q-pa-md">
    <div class="q-col-gutter-md row items-start">
      <div class="col-4">
    <q-img
          src="https://www.veleri.hr/studisweb/images/veleri_back.png"
    />

  </div>
  </div>
  </div>
  <div class="q-pa-md">
    <q-carousel
      animated
      v-model="slide"
      arrows
      navigation
      infinite
    >
      <q-carousel-slide :name="1" img-src="https://www.veleri.hr/studisweb/images/veleri_back.png" />
      <q-carousel-slide :name="2" img-src="https://cdn.quasar.dev/img/parallax1.jpg" />
      <q-carousel-slide :name="3" img-src="https://cdn.quasar.dev/img/parallax2.jpg" />
      <q-carousel-slide :name="4" img-src="https://cdn.quasar.dev/img/quasar.jpg" />
    </q-carousel>
  </div>
  <div class="q-pa-lg flex flex-left">
    <q-pagination
      v-model="current"
      :max="5"
      :input="true"
    >
    </q-pagination>
  </div>
  <div>
     <q-btn color="blue" text-color="black" class="absolute" style="right: 0; right: 200px; transform: translateY(50%);" label="Izbriši" />
      <q-btn color="blue" text-color="black" class="absolute" style="right: 0; right: 100px; transform: translateY(50%);" label="Uredi" />
    </div>
  </q-page>
</template>

<style>

</style>

<script>
export default {
  data () {
    return {
      posts: [],
      current: 3,
      slide: 1,
      vrsta: ''
    }
  },
  created () {
    this.$axios.get('http://193.198.97.14:8000/api/biljnevrste/3/?format=json')
      .then((response) => {
        this.vrsta = response.data
      })
      .catch(() => {
        this.$q.notify({
          message: 'Loading failed'
        })
      })
  },
  methods: {
  }
}

</script>
