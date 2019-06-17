<template>
  <q-page padding>
      <div class="row" style="justify-content: center;">
        <div>
        <q-tabs
        v-model="tab"
        inline-label
      >
        <q-tab name="unos" label="Unos" />
        <q-tab name="pregled" label="Pregled" />
        <q-tab name="kviz" label="Kviz" />
      </q-tabs>
      </div>
      </div>
    <div class="q-pa-lg">
      <div class="row" style="justify-content: center;">
        <img alt="Quasar logo" src="~assets/quasar-logo-full.svg">
      </div>
    </div>
    <div class="q-pa-lg">
      <q-input v-model="text" placeholder="Hrvatski naziv" />
    </div>
    <div class="q-pa-lg">
      <q-input v-model="text" placeholder="Latinski naziv" />
    </div>
    <div class="q-pa-lg row">
      <div class="col">
        <q-list no-border>
          <q-list-header>Uporabni dio</q-list-header>
        </q-list>
        <div class="q-gutter-sm">
              <q-checkbox v-model="izbor1" label="Izbor 1" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="izbor2" label="Izbor 2" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="izbor3" label="Izbor 3" />
        </div>
      </div>
      <div class="col">
        <q-list no-border>
          <q-list-header>Bioaktivna tvar</q-list-header>
        </q-list>
        <div class="q-gutter-sm">
              <q-checkbox v-model="izbor1" label="Izbor 1" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="izbor2" label="Izbor 2" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="izbor3" label="Izbor 3" />
        </div>
      </div>
    </div>
    <div class="row" style="justify-content: flex-end;">
        <div class="q-pa-lg right" >
            <q-btn color="red" text-color="white" label="Završi" />
        </div>
        <div class="q-pa-lg right">
            <q-btn color="blue" text-color="white" label="Provjeri" />
        </div>
        <div class="q-pa-lg right">
            <q-btn @click="randomLink" :to="kvizLink" color="green" text-color="white" label="Novo pitanje" />
        </div>
    </div>
  </q-page>
</template>

<q-toolbar-title>
  Layout Header
  <span slot="subtitle">Optional subtitle</span>
</q-toolbar-title>

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
