<template>
    <q-page padding="">
      <div class="window-height window-width row justify-center items-center">
      <q-list bordered padding class="rounded-borders" style="width: 1300px">
        <div class="q-pa-lg row justify-center">
          <div class="col">
            <q-editor rounded outlined v-model="post.body" :definitions="definitions"/>
          </div>
          <div class="row justify-center">
          <div class="col">
          <q-list bordered padding class="rounded-borders" style="max-width: 300px">
            <q-item-label header>Odaberi uporabni dio:</q-item-label>
            <q-item  v-for="dio in uporabnidijelovi" :key="dio.id" class="q-my-sm" clickable v-ripple>
              <q-item-section>
                <q-radio v-model='radioU' :val=dio.naziv />
              </q-item-section>
              <q-item-section>
                <q-item-label title>{{ dio.naziv }}</q-item-label>
              </q-item-section>
            </q-item>
            </q-list>
            </div>
            </div>
            </div>
            <div class="q-pa-lg row justify-center">
              <div>
                  <q-btn color="primary" text-color="black" label="SPREMI" @click="spremiSliku"/>
              </div>
          </div>
          </q-list>
          </div>
    </q-page>
</template>

<script>

export default {
  data () {
    return {
      hrvatskiNaziv: '',
      radioS: '',
      radioR: '',
      radioV: '',
      radioU: '',
      radioB: '',
      uporabnidijelovi: [],
      post: '',
      definitions: {
        insert_img: {
          tip: 'Insert Image',
          icon: 'photo',
          handler: this.insertImg // handler will call insertImg() method
        }
      }
    }
  },
  methods: {
    insertImg () { // insertImg method
      const post = this.post
      // create an input file element to open file dialog
      const input = document.createElement('input')
      input.type = 'file'
      input.accept = '.png, .jpg' // file extensions allowed
      let file
      input.onchange = _ => {
        const files = Array.from(input.files)
        file = files[0]
        // lets load the file as dataUrl
        const reader = new FileReader()
        let dataUrl = ''
        reader.onloadend = function () {
          dataUrl = reader.result
          // append result to the body of your post
          post.body += '<div><img src="' + dataUrl + '" /></div>'
        }
        reader.readAsDataURL(file)
      }
      input.click()
    },
    unosPodataka () {
      this.$axios.post('/uporabnidijelovi', {
        url: 'http://193.198.97.14:8000/api/uporabnidijelovi/8/',
        naziv: 'Test'
      })
        .then(function (response) {
          console.log(response)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    fetchUporabniDijelovi () {
      this.$axios.get('http://193.198.97.14:8000/api/uporabnidijelovi/?format=json')
        .then((response) => {
          this.uporabnidijelovi = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created () {
    this.fetchUporabniDijelovi()
  }
  // spremiSliku
}
</script>
