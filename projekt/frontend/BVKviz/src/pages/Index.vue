<template>
  <q-page padding>
    <div class="q-pa-xl text-weight-bold q-display-2">
    </div>
    <div class="q-pa-lg">
      <div class="image_container">
        <div>
          <img alt="Quasar logo" src="~assets/quasar-logo-full.svg">
        </div>
        <div>
          <q-radio v-model="radioS" val="Izbor 1" />
        </div>
      </div>
      <div class="image_container">
        <div>
          <img alt="Quasar logo" src="~assets/quasar-logo-full.svg">
        </div>
        <div>
          <q-radio v-model="radioS" val="Izbor 2" />
        </div>
      </div>
      <div class="image_container">
        <div>
          <img alt="Quasar logo" src="~assets/quasar-logo-full.svg">
        </div>
        <div>
          <q-radio v-model="radioS" val="Izbor 3" />
        </div>
      </div>
      <div class="image_container">
        <div>
          <img alt="Quasar logo" src="~assets/quasar-logo-full.svg">
        </div>
        <div>
          <q-radio v-model="radioS" val="Izbor 4"/>
        </div>
      </div>
      <div class="image_container">
        <div>
          <img alt="Quasar logo" src="~assets/quasar-logo-full.svg">
        </div>
        <div>
          <q-radio v-model="radioS" val="Izbor 5"/>
        </div>
      </div>
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
            <q-radio v-model='radio1' val="Izbor 1" />
          </q-item-side>
          <q-item-main>
            <q-item-tile title>Izbor 1</q-item-tile>
          </q-item-main>
        </q-item>
        <q-item>
          <q-item-side>
            <q-radio v-model='radio1' val="Izbor 2" />
          </q-item-side>
          <q-item-main>
            <q-item-tile title>Izbor 2</q-item-tile>
          </q-item-main>
        </q-item>
        <q-item>
          <q-item-side>
            <q-radio v-model='radio1' val="Izbor 3" />
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
      <q-btn color="white" text-color="black" label="Zavrsi" />
      <q-btn color="white" text-color="black" label="Provjeri" />
      <q-btn color="white" text-color="black" label="Dalje" />
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
  methods: {
    loadData () {
      this.$axios.get('http://193.198.97.14:8000/api/rodovi/1')
        .then((response) => {
          this.data = response.data
          alert(this.data)
        })
        .catch(() => {
          this.$q.notify({
            color: 'negative',
            position: 'top',
            message: 'Loading failed',
            icon: 'report_problem'
          })
          alert(this.data)
        })
    }
  },
  created () {
    this.loadData()
  },
  data () {
    return {
      radio1: 'two',
      radio2: 'one',
      radioS: 'slika',
      group: 'upload',
      list: ''
    }
  }
}
</script>
