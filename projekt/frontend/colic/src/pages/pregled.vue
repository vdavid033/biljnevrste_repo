<template>
    <q-page padding="">
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
      <div class="row">
        <div class="col-3">
          <div class="q-pa-md">
              <q-label>Uporabni dio</q-label>
            <div class="q-gutter-sm">
              <q-checkbox v-model="herba" label="herba" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="cvat" label="cvat" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="korjen" label="korijen" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="pupoljak" label="gigantski terminalni pupoljak" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="stabljika" label="stabljika" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="hipokotil" label="zadebljali hipokotil" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="cvijet" label="cvijet" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="plod" label="plod" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="list" label="list" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="petiljka" label="petiljka" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="gomolj" label="gomolj" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="sjeme" label="sjeme" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="zadebljalikorjen" label="zadebljali korijen" />
            </div>
            <div class="q-px-sm">
            </div>
          </div>
        </div>
        <div class="col-9 vertical-center-align">
          <div class="row search-row">
          <div>
          <label>Bioaktivna tvar: </label>
          <input type="text" v-model="search" placeholder="search" />
        </div>
          </div>
          <div class="row main-row">
        <table class="q-table responsive" style="height: 100%;">
  <thead>
    <tr>
      <th>Botanička porodica (lat.)</th>
      <th>Rod (lat.)</th>
      <th>Porodica (hrv.)</th>
        <th>Vrsta</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="text-center">Botanička porodica #1</td>
      <td class="text-center">1</td>
      <td class="text-center">1</td>
      <td class="text-center">1</td>
    </tr>
    <tr>
     <td class="text-center">Botanička porodica #2</td>
      <td class="text-center">2</td>
      <td class="text-center">2</td>
      <td class="text-center">2</td>
    </tr>
    <tr>
      <td class="text-center">Botanička porodica #3</td>
      <td class="text-center">3</td>
      <td class="text-center">3</td>
      <td class="text-center">3</td>
    </tr>
    <tr>
      <td class="text-center">Botanička porodica #4</td>
      <td class="text-center">4</td>
      <td class="text-center">4</td>
      <td class="text-center">4</td>
    </tr>
  </tbody>
</table>
</div>
<div class="row button-row">
   <q-btn color="green" text-color="black" label="PRIKAZ" />
  </div>
</div>
</div>
    </q-page>
</template>

<script>
export default {
  loadData () {
    this.$axios.get('http://193.198.97.14:8000/api/porodice/1/?format=api')
      .then((response) => {
        this.data = response.data
      })
      .catch(() => {
        this.$q.notify({
          message: 'Loading failed'
        })
      })
  },
  data () {
    return {
      myInput: '',
      text: '',
      herba: true,
      cvat: true,
      korjen: true,
      pupoljak: true,
      stabljika: true,
      hipokotil: true,
      cvijet: true,
      plod: true,
      list: true,
      petiljka: true,
      gomolj: true,
      sjeme: true,
      zadebljalikorjen: true,
      post: []
    }
  },
  methods: {
    handleClick () {
      this.myInput = 'clicked'
    }
  }
}
</script>

  function newFunction() {
    return null;
  }
