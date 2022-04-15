function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    $(".g-signin2").css("display", "none");
    $(".textinfo").css("display", "none");
    console.log(profile.getEmail());
    var email = profile.getEmail();
    var accessToken = googleUser.wc.access_token;
    if (email.includes("@findfilo.com")) {
        $(".data").css("display", "block");
        $(".container").css("display", "block");
        $(".containerr").css("display", "block");
        $(".emaill").text(profile.getEmail());
        const imageForm = document.getElementById('image-upload-form');
        imageForm.addEventListener('submit',async function (e) {
            e.preventDefault();
            const data = document.getElementById('file-ip-1')
            const formData = new FormData();
            formData.append('file',data.files[0]); 
            const baseUrl = window.location.host

            const resp =await fetch("http://"+baseUrl+'/upload/image', {
                method: 'POST',
                body: formData,
                headers: {"Authorization": accessToken }
            });
            const response = await resp.json();

            renderUrl(response.url)
        });
        };
        return;
        
    }

    function dontGo(event) {
        event.preventDefault();
    }

    function renderUrl(data) {
        var box = document.getElementById('text_input')
        box.value = data;
        return;
    }
    
    function signOut() {
        var auth2 = gapi.auth2.getAuthInstance();
        auth2.signOut().then(function () {
            alert("You have been signed out successfully");
            $(".data").css("display", "none");
            $(".g-signin2").css("display", "block");
            $(".container").css("display", "none");
            $(".containerr").css("display", "none");
        }).catch(function(err) {
            console.log(err)
        });
        localStorage.clear();
        return;
    }    

    function copyTextContent() {
        var data = document.getElementById('text_input').value
        navigator.clipboard.writeText(data);
        window.setTimeout('alert("URL Copied");window.close();', 1);
        return;
    }

    function showPreview(event){
        if(event.target.files.length > 0){
          var src = URL.createObjectURL(event.target.files[0]);
          var preview = document.getElementById("file-ip-1-preview");
          preview.src = src;
          preview.style.display = "block";
        }
        return;
      }