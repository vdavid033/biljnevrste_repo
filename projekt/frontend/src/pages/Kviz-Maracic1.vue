<template>
  <q-page padding>
    <div class="q-pa-lg">
      slika biljke
      <div>
        <img alt="Quasar logo" src="~assets/quasar-logo-full.svg">
      </div>
    </div>
    <div class="q-pa-lg">
      Hrvatski naziv
      <q-input v-model="text" placeholder="Hrvatski naziv" />
    </div>
    <div class="q-pa-lg">
      Latinski naziv
      <q-input v-model="text" placeholder="Latinski naziv" />
    </div>
    <div class="q-pa-lg row">
      <div class="col">
       Uporabni dio
        <q-list no-border>
          <q-list-header>Uporabni dio</q-list-header>
        </q-list>
        <q-item>
          <q-item-side>
            <q-radio v-model="radio1" val="Izbor 1" />
          </q-item-side>
          <q-item-main>
            <q-item-tile title>Izbor 1</q-item-tile>
          </q-item-main>
        </q-item>
        <q-item>
          <q-item-side>
            <q-radio v-model="radio1" val="Izbor 2" />
          </q-item-side>
          <q-item-main>
            <q-item-tile title>Izbor 2</q-item-tile>
          </q-item-main>
        </q-item>
        <q-item>
          <q-item-side>
            <q-radio v-model="radio1" val="Izbor 3" />
          </q-item-side>
          <q-item-main>
            <q-item-tile title>Izbor 3</q-item-tile>
          </q-item-main>
        </q-item>
      </div>
      <div class="col">
        Bioaktivna tvar
        <q-list no-border>
          <q-list-header>Bioaktivna tvar</q-list-header>
        </q-list>
        <q-item>
          <q-item-side>
            <q-radio v-model="radio2" val="Izbor 1" />
          </q-item-side>
          <q-item-main>
            <q-item-tile title>Izbor 1</q-item-tile>
          </q-item-main>
        </q-item>
        <q-item>
          <q-item-side>
            <q-radio v-model="radio2" val="Izbor 2" />
          </q-item-side>
          <q-item-main>
            <q-item-tile title>Izbor 2</q-item-tile>
          </q-item-main>
        </q-item>
        <q-item>
          <q-item-side>
            <q-radio v-model="radio2" val="Izbor 3" />
          </q-item-side>
          <q-item-main>
            <q-item-tile title>Izbor 3</q-item-tile>
          </q-item-main>
        </q-item>
      </div>
    </div>
    <div class="q-pa-lg right">
      Gumbi
      <q-btn color="red" text-color="white" label="Zavrsi" />
      <q-btn color="blue" text-color="white" label="Provjeri" />
      <q-btn @click="randomLink" :to="kvizLink" color="green" text-color="white" label="Novo pitanje" />
    </div>
  </q-page>
</template>
<style>
</style>

<script>
export default {
  data () {
    return {
      links: ['kviz1', 'kviz2'],
      kvizLink: 'kviz2'
    }
  },
  methods: {
    randomLink (e, go) {
      e.navigate = false
      // this.kvizLink = this.links[Math.floor(Math.random() * 2)]
      setTimeout(() => {
        go()
      }, 1)
    }
  },
  created () {
  }
}
</script>
