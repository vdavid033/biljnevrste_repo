<template>
    <q-page padding="">
        <div class="row gutter-xs">
            <div class="col">
                Hrvatski naziv:
                <div>
                    <q-input outlined v-model="myInput" label="Outlined" />
                </div>
            </div>
            <div class="col">
                Sinonim:
                <div>
                    <q-input outlined v-model="myInput" label="Outlined" />
                </div>
            </div>
        </div>
        <div class="row gutter-xs">
            <div class="col">
                Latinski naziv:
            </div>
            <div class="col">
                Rod:
                <div>
                    <q-input outlined v-model="myInput" label="Outlined" />
                </div>
            </div>
            <div class="col">
                <div class="col">
                Vrsta:
                <div>
                    <q-input outlined v-model="myInput" label="Outlined" />
                </div>
            </div>
            </div>
            <div class="col">
                Podvrsta-ssp.:
                <div>
                    <q-input outlined v-model="myInput" label="Outlined" />
                </div>
            </div>
            <div class="col">
                Varijetet:
                <div>
                    <q-input outlined v-model="myInput" label="Outlined" />
                </div>
            </div>
            <div class="col">
                <div class="col">
                Sistemtičar:
                <div>
                    <q-input outlined v-model="myInput" label="Outlined" />
                </div>
            </div>
          </div>
          </div>
        <div class="q-pa-md" style="max-width: 300px">
          <div class="q-gutter-md">
            <q-select square filled v-model="model" :options="options" label="Square filled" />
          </div>
        </div>
        <div class="row gutter-xs">
            <div class="col">
                Botanicka porodica:
                <div>
                    <q-input outlined v-model="myInput" label="Outlined" />
                </div>
            </div>
            <div class="col">
                Dodaj novu lat. kat.:
                <div>
                    <q-input outlined v-model="myInput" label="Outlined" />
                </div>
            </div>
            <div class="col">
                <div class="col">
                Dodaj novu hrv. kat.:
                <div>
                    <q-input outlined v-model="myInput" label="Outlined" />
                </div>
            </div>
            </div>
          <div class="col">
              <div>
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
              </div>
          </div>
        </div>
        <div class="row gutter-xs">
          <div class="col">
              Uporabni dio:
              <div>
                  <q-select v-model="model" :options="options" label="Standard" />
              </div>
          </div>
          <div class="col">
              Bioaktivna tvar:
              <div>
                  <q-input outlined v-model="myInput" label="Outlined" />
              </div>
          </div>
          <div class="col">
              <div class="col">
              Opis biljke:
              <div>
                  <q-input outlined v-model="myInput" label="Outlined" />
              </div>
          </div>
          </div>
        </div>
          <div class="q-pa-md">
            <div class="q-gutter-sm">
              <q-checkbox v-model="herba" label="herba" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="cvat" label="cvat" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="korjen" label="korjen" />
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
              <q-checkbox v-model="zadebljalikorjen" label="zadebljali korjen" />
            </div>
            <div class="q-gutter-sm">
              <q-checkbox v-model="teal" label="dodaj" />
            </div>

            <div class="q-px-sm">
            </div>
          </div>
        <div class="row gutter-xs">
          <div class="col">
              Učitavanje slika:
          </div>
          <div class="col">
              <div>
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
                  <q-btn round color="primary" label="+" text-color="black" @click="handleClick" />
              </div>
          </div>
        <div class="row gutter-xs">
          <div class="col">
              <div>
                  <q-btn color="white" text-color="black" label="SPREMI" />
              </div>
          </div>
        </div>
        </div>
    </q-page>
</template>

<script>
export default {
  data () {
    return {
      myInput: '',
      text: '',
      model: null,
      options: [
        'jedan', 'dva', 'tri', 'cetiri', 'pet'
      ],
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
      zadebljalikorjen: true

    }
  },
  methods: {
    handleClick () {
      this.myInput = 'clicked'
    }
  }
}
</script>
