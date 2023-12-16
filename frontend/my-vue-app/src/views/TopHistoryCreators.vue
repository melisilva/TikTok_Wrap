<template>
     <img class="tik-tok-logo" src="../assets/images/tiktok-logo.png" />
     <div id="your-component-id" class="page" style="background: #b4b5db;">
     <!--<button @click="captureAndSave">Save Image</button> -->
          <div class="row">
               <div class="top-history-creators"> Your Top 5 Watched Creators</div>
          </div>
          <br style="margin-bottom: 10px; "/>
          <div class="row">
               <div class="side-by-side-chart" style="flex-direction: row; width: 100%; ">
                    <div class="col ranking" >
                         <div class="place ranking">
                              <img class="ellipse ranking" v-bind:src="photos[4] === '' ? 'src/assets/images/user_default.png' : photos[4]" />
                              <div class="rectangle-place" style=" width: auto; top: -22.5px; z-index: 1; padding: 2px 5px 2px 5px;">
                                   <p class="number-placement">#5</p>
                              </div>
                         </div>
                         <div class="rectangle" id="rect-15">
                              <p class="text-inside-rectangle"> {{ creators[4]}} </p>
                         </div>
                    </div>
                    <div class="col ranking">
                         <div class="place ranking">
                              <img class="ellipse ranking" v-bind:src="photos[1] === '' ? 'src/assets/images/user_default.png' : photos[1]" />
                              <div class="rectangle-place" style=" width: auto; top: -22.5px; z-index: 1; padding: 2px 5px 2px 5px;">
                                   <p class="number-placement">#2</p>
                              </div>
                         </div>
                         <div class="rectangle" id="rect-12">
                              <p class="text-inside-rectangle"> {{ creators[1]}} </p>
                         </div>
                    </div>
                    <div class="col ranking">
                         <div class="place ranking">
                              <img class="ellipse ranking" v-bind:src="photos[0] === '' ? 'src/assets/images/user_default.png' : photos[0]" />
                              <div class="rectangle-place" style=" width: auto; top: -22.5px; z-index: 1; padding: 2px 5px 2px 5px;">
                                   <p class="number-placement">#1</p>
                              </div>
                         </div>
                         <div class="rectangle" id="rect-11">
                              <p class="text-inside-rectangle"> {{ creators[0]}} </p>
                         </div>
                    </div>
                    <div class="col ranking">
                         <div class="place ranking">
                              <img class="ellipse ranking" v-bind:src="photos[2] === '' ? 'src/assets/images/user_default.png' : photos[2]" />
                              <div class="rectangle-place" style=" width: auto; top: -22.5px; z-index: 1; padding: 2px 5px 2px 5px;">
                                   <p class="number-placement">#3</p>
                              </div>
                         </div>
                         <div class="rectangle" id="rect-13">
                              <p class="text-inside-rectangle"> {{ creators[2]}} </p>
                         </div>
                    </div>
                    <div class="col ranking">
                         <div class="place ranking">
                              <img class="ellipse ranking" v-bind:src="photos[3] === '' ? 'src/assets/images/user_default.png' : photos[3]" />
                              <div class="rectangle-place" style=" width: auto; top: -22.5px; z-index: 1; padding: 2px 5px 2px 5px;">
                                   <p class="number-placement">#4</p>
                              </div>
                         </div>
                         <div class="rectangle" id="rect-14">
                              <p class="text-inside-rectangle"> {{ creators[3]}} </p>
                         </div>
                    </div>
     
     
               </div>
          </div>
          
     </div>
</template>


<script>
import axios from 'axios'
import { defineComponent } from 'vue'
import html2canvas from 'html2canvas';

export default defineComponent({
  name: 'TopHistoryCreators',
  data() {
    return {
     creators: [],
     photos: []
    }
  },
  methods: {
    async captureAndSave() {
      // Use html2canvas to capture the content
      const element = document.getElementById('your-component-id'); // Replace with your component's ID
      const canvas = await html2canvas(element);

      // Convert canvas to image
      const image = canvas.toDataURL('image/png');

      // Create a download link
      const link = document.createElement('a');
      link.href = image;
      link.download = 'top_creators.png';
      document.body.appendChild(link);

      // Trigger the download
      link.click();

      // Remove the link from the DOM
      document.body.removeChild(link);
    },
  },
  async beforeMount() {
    await axios.get("http://localhost:8000/top-creator-history")
      .then((response) => {
        console.log(response.data)
        this.creators = Object.values(response.data['Username']);
        this.photos = Object.values(response.data['Photo']);
      })
      .catch((error) => {
        console.log(error)
      })
  }
})
</script>