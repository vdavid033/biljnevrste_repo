<template>
    <q-page padding="">
      <div class="row" style="justify-content: center;">
      </div>
        <div class="row space-between">
            <div clas="col-6" style="width: 45%; margin-right: 5%;">
                    <q-input outlined v-model="text" label="Hrvatski naziv" :dense="dense" />
            </div>
            <div class="col-6" style="width: 45%; margin-left: 5%;">
                <q-input outlined v-model="text" label="Sinonim" :dense="dense" />
            </div>
        </div>
        <div class="row space-between" style="font-size: 1.2em;">
                Latinski naziv
        </div>
        <div class="row space-between">
            <div class="col-4" style="width: 30%; margin-right: 5%;">
                <q-input outlined v-model="text" label="Rod" :dense="dense" />
            </div>
            <div class="col-4" style="width: 30%; margin-right: 5%;">
                <q-input outlined v-model="text" label="Vrsta" :dense="dense" />
            </div>
            <div class="col-4" style="width: 30%;">
                <q-input outlined v-model="text" label="Podvrsta - SSP." :dense="dense" />
            </div>
        </div>
        <div class="row space-between">
            <div class="col-6" style="width: 45%; margin-right: 5%;">
               <q-input outlined v-model="text" label="Varijetet" :dense="dense" />
            </div>
            <div class="col-6" style="width: 45%; margin-left: 5%;">
                <q-input outlined v-model="text" label="Sistematičar" :dense="dense" />
          </div>
          </div>
        <div class="row" style="font-size: 1.2em; padding-bottom: 3.5%;">
            <div class="col-3" style="width: 27.5%; margin-right: 5%;">
                <div>
                <q-btn-dropdown label="Botanička porodica:">
                  <!-- dropdown content -->
                  <q-list link>
                    <q-item>
                      <q-item-main>
                        <q-item-tile>Primjer</q-item-tile>
                      </q-item-main>
                    </q-item>
                  </q-list>
                </q-btn-dropdown>
                </div>
            </div>
            <div class="col-3" style="width: 27.5%; margin-right: 5%;">
                <q-input outlined v-model="text" label="Dodaj novu lat. kat." :dense="dense" />
            </div>
            <div class="col-3" style="width: 27.5%; margin-right: 5%;">
                <q-input outlined v-model="text" label="Dodaj novu hrv. kat." :dense="dense" />
            </div>
          <div class="col-3" style="width: 2%; margin: auto;">
              <div style="display: flex; justify-content: center;">
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick"  />
              </div>
          </div>
        </div>
        <div class="row">
          <div class="col-5">
              Uporabni dio:
              <div class="q-pa-md">
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
            <div class="q-gutter-sm">
              <q-checkbox v-model="teal" label="dodaj" />
            </div>

            <div class="q-px-sm">
            </div>
          </div>
          </div>
          <div class="col-7">
              <div class="row" style="padding-bottom: 5%;">
              <q-input outlined v-model="text" style="width: 100%;" label="Bioaktivna tvar" :dense="dense" />
              </div>
              <div class="row" style="width: 100%; height: 50%;">
              <q-input outlined v-model="text" style="width: 100%;height: 100%;" class="big-input" label="Opis biljke" :dense="dense" />
              </div>
          </div>
        </div>
        <div class="row space-between" style="font-size: 1.2em;">
              Učitavanje slika
        </div>
        <div class="row space-between" style="justify-content: space-evenly;">
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
        </div>
        <div class="row space-between" style="justify-content: flex-end;">
              <div>
                  <q-btn color="white" text-color="black" label="SPREMI" />
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
      loading: true,
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
