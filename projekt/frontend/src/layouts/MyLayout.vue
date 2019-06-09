<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-toolbar-title>
          Biljne Vrste
          </q-toolbar-title>
          <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 1600px">
      <q-tabs
        v-model="tab"
        class="bg-primary text-white shadow-2"
      >
        <q-tab name="unos" @click="idinaUnos" label="Unos Biljaka">
          <q-badge color="red" floating></q-badge>
        </q-tab>
        <q-tab name="pregled" @click="idinaPregled" label="Pregled Biljaka">
          <q-badge color="red" floating></q-badge>
        </q-tab>
        <q-tab name="kviz" @click="idinaKviz" label="Pregled rezultata kviza">
          <q-badge color="red" floating></q-badge>
        </q-tab>
      </q-tabs>
    </div>
    </div>
  </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>
<script>
export default {
  methods: {
    idinaUnos () {
      this.$router.push({ path: '/unos' })
    },
    idinaPregled () {
      this.$router.push({ path: '/pregled' })
    },
    idinaKviz () {
      this.$router.push({ path: '/kviz' })
    }
  },
  data () {
    return {
      tab: ''
    }
  }
}
</script>

<style>
</style>
