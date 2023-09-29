

rt default function handleResponseFromAPI(promise) {
	  return promise
	    .then(() => ({ status: 200, body: 'success' }))
	    .catch(() => Error())
	    .finally(() => { console.log('Got a response from the API'); });
}
              aria-label="Varad on Github" href="http://github.com/billkolos" class="hoverline"
              target="_blank">github.com/billkolos</a></a>
