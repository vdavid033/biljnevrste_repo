<template>
    <div class="q-pa-lg row">
        <div class="col">
        <q-editor v-model="post.body" :definitions="definitions"/>
      </div>
    </div>
</template>

<script>

export default {
  data () {
    return {
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
      this.$axios.post('/user', {
        firstName: 'Fred',
        lastName: 'Flintstone'
      })
        .then(function (response) {
          console.log(response)
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>
