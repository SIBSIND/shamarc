//scgi 
//cached 
 
		
var IKLAD_FUNC = {
	get_cookie: function ( check_name ) {
		var a_all_cookies = document.cookie.split( ';' );
		var a_temp_cookie = '';
		var cookie_name = '';
		var cookie_value = '';
		var b_cookie_found = false;
	
		for ( i = 0; i < a_all_cookies.length; i++ )	{
			a_temp_cookie = a_all_cookies[i].split( '=' );
			cookie_name = a_temp_cookie[0].replace(/^\s+|\s+$/g, '');
			if ( cookie_name == check_name ){
				b_cookie_found = true;
				if ( a_temp_cookie.length > 1 ){
					cookie_value = unescape( a_temp_cookie[1].replace(/^\s+|\s+$/g, '') );
				};
				return cookie_value;
				break;
			};
			a_temp_cookie = null;
			cookie_name = '';
		}
		if ( !b_cookie_found )	{
			return null;
		}
	},

	set_cookie: function ( name, value, expires_min, path, domain, secure ) {
		var today = new Date();
		today.setTime( today.getTime() );
		
		if ( expires_min ) {
			expires_min = expires_min * 1000 * 60;
		};
		var expires_date = new Date( today.getTime() + (expires_min) );
		
		document.cookie = name + "=" + escape( value ) +
		( ( expires_min ) ? ";expires=" + expires_date.toGMTString() : "" ) +
		( ( path ) ? ";path=" + path : "" ) +
		( ( domain ) ? ";domain=" + domain : "" ) +
		( ( secure ) ? ";secure" : "" );
	},
	
	delete_cookie: function ( name, path, domain ) {
		if ( IKLAD_FUNC.get_cookie( name ) ) {
			document.cookie = name + "=" + ( ( path ) ? ";path=" + path : "") + 
			( ( domain ) ? ";domain=" + domain : "" ) + 
			";expires=Thu, 01-Jan-1970 00:00:01 GMT";
		};
	},
	
	object_to_string: function (obj) {
		var has_NL = false;
		var NL_SPL = '<NL>';
		
		for (var v in obj) {
			if (obj[v] == null) {
				obj[v] = '';
			};
		};
		
		for (var v in obj) {
			if (obj[v].toString().indexOf("\n") >= 0) {
				has_NL = true;
				break;
			};
		};
		
		if (has_NL) {
			while (1) {
				NL_SPL += Math.floor(Math.random() * 10);
				var NL_found = false;
				
				for (var v in obj) {
					if (obj[v].toString().indexOf(NL_SPL) >= 0) {
						NL_found = true;
						break;
					};
				};
				
				if (NL_found) {
					continue;
				} else {
					break;
				};
			};
			
			
			for (var v in obj) {
				obj[v] = obj[v].toString().replace(/\n/g, NL_SPL);
			};
			obj._NL = NL_SPL;
		};
		
		
		var s = '';
		for (var v in obj) {
			s += v + ':' + obj[v].toString() + "\n";
		};
		
		return s;
	},
	
	string_to_object: function (str) {
		var obj = new Object;
		
		var lines = str.split("\n");
		
		for (var i=0; i < lines.length; i++) {
			var line = lines[i];
			
			if (line.match(/^(.*?):((.|\r)*)$/)) {
				obj[RegExp.$1] = RegExp.$2;
			};
		};
		
		if (typeof obj._NL != 'undefined') {
			var rx = new RegExp(obj._NL, 'g');
			for (var v in obj) {
				obj[v] = obj[v].toString().replace(rx, "\n");
			};
		};
		
		delete obj._NL;
		return obj;
	},

	find_object_position: function (obj) {
	  var curleft = 0;
	  var curtop = 0;
	   
	  if (obj.offsetParent) {
	    while(1)  {
	      curleft += obj.offsetLeft;
	      curtop += obj.offsetTop;
	      obj = obj.offsetParent;
	      if (! obj) { break; };
	    };
	  } else  {
	  	if(obj.x) curleft += obj.x;
	    if(obj.y) curtop += obj.y;
	  };
	  
	  return [curleft, curtop];
	}


};

		
		var IKLAD_4524 = {
			client_id: '',
			iframe: '',
			chat_window_open: 0,
			
			curr_operator_status: '',
			CODE_CONTAINER: '',
			
			SYSTEM: {
				INITIALIZED: false,
				ACC_TYPE: 'p'
			},
			
			TEMPLATE: {
				HTML_CODE: '',
				OPINIONS: [
{
 id: 1,
text: 'Super',
want_comment: 0
},
{
 id: 2,
text: 'Good',
want_comment: 0
},
{
 id: 3,
text: 'Normal',
want_comment: 0
},
{
 id: 4,
text: 'Bad',
want_comment: 1
},
{
 id: 5,
text: 'Worst',
want_comment: 1
}
]
			},
			
			OPERATOR_STATUS: {
				current_status: 'online'
			},
			
			AUTO_CMD_POLLER: {
				active: false,
				timer: '',
				last_id : 0,
				poll_time: 30000, //default = each 30 seconds
				
				_MSG_DATA: '',
				
				start: function () {
					if (IKLAD_4524.AUTO_CMD_POLLER.active) return;
			
					IKLAD_4524.AUTO_CMD_POLLER.active = true;
					IKLAD_4524.AUTO_CMD_POLLER.timer = setTimeout('IKLAD_4524.AUTO_CMD_POLLER.poll()', 100);
				},
				
				stop: function () {
					IKLAD_4524.AUTO_CMD_POLLER.active = false;
					clearTimeout(IKLAD_4524.AUTO_CMD_POLLER.timer);
					IKLAD_4524.AUTO_CMD_POLLER.timer = '';
				},
				
				poll: function () {
					if (! IKLAD_4524.AUTO_CMD_POLLER.active) return;
					
					var s = document.createElement('script');
					s.type = 'text/javascript';
					s.charset = 'utf-8';
					s.src = 'https://chat.iklad-chat.biz/outchat_cmd.cgi?c=4524&cid=' + IKLAD_4524.client_id + '&aid=' + IKLAD_4524.AUTO_CMD_POLLER.last_id + '&v=2&u=' + escape(window.location.href.slice(7)) + '&r=' + Math.random();
					IKLAD_4524.CODE_CONTAINER.appendChild(s);
				},
				
				
				on_message: function (msg_id, msg_data) {
					if (! IKLAD_4524.AUTO_CMD_POLLER.active) return;	//this can happen, coz script loading can be initiated before chat window opened

					IKLAD_4524.AUTO_CMD_POLLER.last_id = msg_id;
					
					//we should NOT call 'notify_received' here. (it will be called by 'outchat_cmd' script if needed)
					
					//display msg in HINT box
					if ((typeof IKLAD_HINT_4524 == 'object') && (typeof IKLAD_HINT_4524.show == 'function')) {
						var coords_descr = IKLAD_STATUS_4524.get_hint_box_coords();
						
						if (coords_descr) {
							IKLAD_HINT_4524.show(msg_data, coords_descr);
						};
					};
				},
				
				notify_received: function (msg_id, options) {
					options.force = typeof options.force == 'undefined' ? false : options.force;
					options.is_auto = typeof options.is_auto == 'undefined' ? true : options.is_auto;
					
					if (! options.force) {
						if (! IKLAD_4524.AUTO_CMD_POLLER.active) return;
					};
					
					var s = document.createElement('script');
					s.type = 'text/javascript';
					s.charset = 'utf-8';
					s.src = 'https://channel4524.iklad-chat.biz/send/c=4524&id=' + IKLAD_4524.client_id + '&cmd=offchat_msg_received/' + (options.is_auto ? 1 : 0) + ',' + msg_id + '/' + Math.random();
					
					IKLAD_4524.CODE_CONTAINER.appendChild(s);
				}
			},
		
			AUTO_DIE: {
				active: false,
				timer: '',
				died: false,
				
				start: function () {
					if (IKLAD_4524.AUTO_DIE.active) return;
					
					IKLAD_4524.AUTO_DIE.timer = setTimeout('IKLAD_4524.AUTO_DIE.die()', 1000*300);
					IKLAD_4524.AUTO_DIE.active = true;
				},
				
				stop: function () {
					IKLAD_4524.AUTO_DIE.active = false;
					
					clearTimeout(IKLAD_4524.AUTO_DIE.timer);
					IKLAD_4524.AUTO_DIE.timer = null;
					
					
					//if 'stop' called after we 'died' - do UN-die
					if (IKLAD_4524.AUTO_DIE.died) {
						IKLAD_4524.AUTO_DIE.died = false;
						IKLAD_4524.iframe.contentWindow.postMessage('init_wait:' + "\n", '*'); //un-qq!
					};
				},
				
				die: function () {
					//stop communication channel
					IKLAD_4524.iframe.contentWindow.postMessage('de_init_wait:' + "\n", '*'); //un-qq!
					IKLAD_4524.AUTO_DIE.stop();
					
					IKLAD_4524.AUTO_DIE.died = true;
				}
			},
			
			COBROWSE: {
				script_loaded: false,
				queue: [],
				
				load_script: function () {
					var s = document.createElement('script');
					s.type = 'text/javascript';
					s.charset = 'utf-8';
					s.src = 'https://chat.iklad-chat.biz/cobrowse.cgi?c=4524&v=2&cid=' + IKLAD_4524.client_id + '&r=' + Math.random();
					IKLAD_4524.CODE_CONTAINER.appendChild(s);
					
					IKLAD_4524.COBROWSE.script_loaded = true;
				},
				
				add_command_to_queue: function (data) {
					if (! IKLAD_4524.COBROWSE.script_loaded) IKLAD_4524.COBROWSE.load_script();
					
					if (typeof IKLAD_4524.COBROWSE.process_command == 'function') {
						IKLAD_4524.COBROWSE.process_command(data);
					} else {
						IKLAD_4524.COBROWSE.queue.push(data);
					};
				}
			},
		
			generate_client_id: function (in_len) {
				var len = (in_len ? in_len : 30);
				var chars = '_qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890';
				var res = '';
				
				for (i=0; i <= len; i++) {
					var st = Math.floor(Math.random() * chars.length);
					res += chars.substr(st,1);
				};
				
				return res;
			},
			
			check_IKLAD_list_init_allowed: function () {
				var ks = Object.keys(window);
				
				for (var i=0; i < ks.length; i++) {
					if (ks[i] == 'IKLAD_4524') continue;
					
					if (ks[i].match(/^IKLAD_(\d+)$/)) {
						var other_ch = RegExp.$1;
						
						if (typeof window[ks[i]].SYSTEM == 'undefined') continue;
						if (! window[ks[i]].SYSTEM.INITIALIZED) continue;
						
						if (IKLAD_4524.SYSTEM.ACC_TYPE == 'f') {
							return false;
						} else {
							if (window[ks[i]].SYSTEM.ACC_TYPE == 'f') {
								if (window['IKLAD_' + other_ch.toString()].CODE_CONTAINER) {
									window['IKLAD_' + other_ch.toString()].CODE_CONTAINER.innerHTML = '';
								};
							};
						};
					};
					
				};
				
				return true;
			},
		
			init: function () {
				if (IKLAD_4524.SYSTEM.INITIALIZED) return;
				if (! IKLAD_4524.check_IKLAD_list_init_allowed()) return;
				
				if (typeof IKLAD_4524.check_allowed_domains == 'function') {
					if (! IKLAD_4524.check_allowed_domains()) {
						return;
					};
				};
				
				// make CODE_CONTAINER
				if (! document.getElementById('IKLAD_CONTAINER_4524')) {	//create new if not pasted to code 'inplace'
					var container = document.createElement('div');
					container.setAttribute("id", "IKLAD_CONTAINER_4524");
					document.body.appendChild(container);
				};
				
				IKLAD_4524.CODE_CONTAINER = document.getElementById('IKLAD_CONTAINER_4524');
				
				//install OnMessage handler
				IKLAD_4524.add_listener(window, "message", IKLAD_4524.on_message_handler);
				
								
				//get||generate client_id
				if ((typeof IKLAD_POPUP == 'undefined') || (typeof IKLAD_POPUP.client_id == 'undefined')) {
					IKLAD_4524.client_id = IKLAD_FUNC.get_cookie("sitechat_ID_4524");
					if (! IKLAD_4524.client_id) {
						IKLAD_4524.client_id = IKLAD_4524.generate_client_id();
					};
					IKLAD_FUNC.set_cookie("sitechat_ID_4524", IKLAD_4524.client_id, 525948, '/');	//1 year
				} else {
					IKLAD_4524.client_id = IKLAD_POPUP.client_id;
				};
				
				//append form HTML
				var form_container = document.createElement('div');
				form_container.innerHTML = IKLAD_4524.TEMPLATE.HTML_CODE;
				document.body.appendChild(form_container);
								
				try {
					IKLAD_STATUS_4524.init({'operator_status': IKLAD_4524.OPERATOR_STATUS.current_status});
				} catch (e) {};
					
				try {
					IKLAD_HINT_4524.init();
				} catch (e) {};
				
				try {
					IKLAD_TEMPLATE_4524.init({
						'operator_status': IKLAD_4524.OPERATOR_STATUS.current_status,						
						'opinions': IKLAD_4524.TEMPLATE.OPINIONS
					});
				} catch (e) {};
				
				
				//create communication iframe
				IKLAD_4524.iframe = document.createElement('iframe');
				IKLAD_4524.iframe.style.display = 'none';
				IKLAD_4524.iframe.setAttribute('style', 'display:none;');
				IKLAD_4524.iframe.src = "https://channel4524.iklad-chat.biz/iframe.cgi?c=4524&v=2&clientid=" + IKLAD_4524.client_id + '&ssl=' + 1;// + "&r=" + Math.random(1);
				document.body.appendChild(IKLAD_4524.iframe);
				
				IKLAD_4524.SYSTEM.INITIALIZED = true;
			},
		
		
	    add_listener: function (element, event, listener, bubble) {
	      if(element.addEventListener) {
	        if(typeof(bubble) == "undefined") bubble = false;
	        element.addEventListener(event, listener, bubble);
	        return true;
	      } else if (element.attachEvent) {
	        element.attachEvent("on" + event, listener);
	        return true;
	      };
	      
	      return false;
	    },
		
		
			on_message_handler: function (evt) {				
				if (evt.origin != 'https://channel4524.iklad-chat.biz') return;
				
				if (evt.data == 'iframe_ready') {					
					var state_obj = {
						title: document.title,
						curr_url: decodeURIComponent(window.location.href.slice(7)),
						chat_window_open: 0	//start with 0 always
					};
					
					if (document.referrer) {
						state_obj.referrer = decodeURIComponent(document.referrer.slice(7));
					};
					
					//send client_state (if we are NOT in popup)
					if (typeof IKLAD_POPUP == 'undefined') {
						evt.source.postMessage('client_state_data:' + "\n" + JSON.stringify(state_obj), evt.origin);
					};
					
					evt.source.postMessage("init_wait:\n", evt.origin);	//init_wait
					
					
					if (typeof IKLAD_POPUP == 'undefined') {
						var WindowOpenStatus = IKLAD_FUNC.get_cookie("IKLAD.window_open_4524");
						if (WindowOpenStatus && (WindowOpenStatus == 1)) {	//reopen window
							IKLAD_TEMPLATE_4524.open_chat_window();
						} else {
							IKLAD_4524.AUTO_CMD_POLLER.start();
							IKLAD_4524.AUTO_DIE.start();
						};
					} else {
						IKLAD_TEMPLATE_4524.open_chat_window();
					};
								
					return;
				};
				
				
				if (evt.data.match(/get_form_data_reply:\n((.|[\n\r])*)/)) {
					var data = JSON.parse(RegExp.$1);
					if (IKLAD_TEMPLATE_4524.form_data) IKLAD_TEMPLATE_4524.form_data(data);
					
					return;
				};
				
				
				if (evt.data.match(/send_form_data_result:\n((.|[\n\r])*)/)) {
					var result = JSON.parse(RegExp.$1);
					if (IKLAD_TEMPLATE_4524.send_form_data_result) IKLAD_TEMPLATE_4524.send_form_data_result(result);
					
					return;
				};
				
				
				if (evt.data.match(/operator_message:\n((.|[\n\r])*)/)) {
					var msg_obj = JSON.parse(RegExp.$1);
					
					IKLAD_TEMPLATE_4524.on_chat_message(msg_obj);
						
					if (IKLAD_4524.chat_window_open == '0') {	//closed chat window
						if ((msg_obj.to == 'client') && (msg_obj.by_human == '1')) {
							IKLAD_4524.AUTO_CMD_POLLER.notify_received(msg_obj.id, {is_auto: false});
							
							//display msg in HINT box
							if ((typeof IKLAD_HINT_4524 == 'object') && (typeof IKLAD_HINT_4524.show == 'function')) {
								var coords_descr = IKLAD_STATUS_4524.get_hint_box_coords();
								
								if (coords_descr) {
									IKLAD_HINT_4524.show(msg_obj.text, coords_descr);
								};
							};
						};
					};
					
					return;
				};
				
				
				if (evt.data.match(/full_chat_history:\n((.|[\n\r])*)/)) {	
					var msgs_arr = JSON.parse(RegExp.$1);
					IKLAD_TEMPLATE_4524.full_chat_log_data({'msgs': msgs_arr});
					return;
				};
				
				
				if (evt.data.match(/operator_status:\n((.|[\n\r])*)/)) {
					var event_obj = JSON.parse(RegExp.$1);

					IKLAD_4524.curr_operator_status = event_obj.status;

					var status_object = {
						'operator_status': event_obj.status
					};
											
					if (event_obj.status == 'offline') {
						status_object.actions = event_obj.actions;
					};

					if (event_obj.status == 'error') {
						status_object.error_message = event_obj.error_message;
					};

					//notify template(s)
					IKLAD_STATUS_4524.operator_status_changed(status_object);
					IKLAD_TEMPLATE_4524.operator_status_changed(status_object);

					//call api
					if (typeof IKLAD_API_4524 == 'object') {
						
						if ( (event_obj.status == 'online') && (typeof IKLAD_API_4524.onReady_func == 'function') ) {	//this will be true only once per page load
							IKLAD_API_4524.onReady_func();
							IKLAD_API_4524.onReady(undefined);	//reset to undef
						};
						
						if ( (event_obj.status == 'offline') && (typeof IKLAD_API_4524.onReadyOffline_func == 'function') ) {	//this will be true only once per page load
							IKLAD_API_4524.onReadyOffline_func();
							IKLAD_API_4524.onReadyOffline(undefined);	//reset to undef
						};
						
					};
					
					return;
				};
				
				if (evt.data.match(/operator_data:\n((.|[\n\r])*)/)) {
					var event_obj = JSON.parse(RegExp.$1);
					IKLAD_TEMPLATE_4524.operator_data_changed(event_obj);
					return;
				};
				
				if (evt.data.match(/operator_typing:\n((.|[\n\r])*)/)) {
					var event_obj = JSON.parse(RegExp.$1);
					IKLAD_TEMPLATE_4524.operator_activity(event_obj);
					return;
				};
				
				if (evt.data.match(/operator_command:\n((.|[\n\r])*)/)) {
					var event_obj = JSON.parse(RegExp.$1);
				
					if (event_obj.command == 'goto') {
						if (typeof IKLAD_POPUP == 'undefined') {
							window.location.href = event_obj.url;
						} else {
							try {
								window.opener.location.href = event_obj.url;
							} catch (e) {};
						};
					};
					
					if (typeof IKLAD_POPUP != 'undefined') {
						return;	//do not process NEXT commands in popup state
					};
					
					if (event_obj.command == 'openchat') {
						IKLAD_TEMPLATE_4524.open_chat_window();
					};
					
					if (event_obj.command == 'closechat') {
						IKLAD_TEMPLATE_4524.close_chat_window();
					};
											
					if (event_obj.command == 'cobrowse_cmd') {
						IKLAD_4524.COBROWSE.add_command_to_queue(event_obj.data);
					};
					
					return;
				};
				
				
				if (evt.data.match(/jseval:\n((.|[\n\r])*)/)) {
					var event_obj = JSON.parse(RegExp.$1);
					try { eval(event_obj.code); } catch (e) {};
					return;
				};
				
			},
			
			
			
			
			//callbacks from TEMPATE
			notify_window_state_changed: function (params) {
				//params.state: 'open' || 'closed' ( window would not KNOW it is in 'popup' state)

				var this_state = params.state;
				
				if ((this_state == 'open') && (typeof IKLAD_POPUP != 'undefined')) {
					this_state = 'popup';
				};
				
				if (this_state == 'open') {
					IKLAD_4524.chat_window_open = 1;
				};
				
				if (this_state == 'popup') {
					IKLAD_4524.chat_window_open = 2;
				};
				
				if (this_state == 'open' || this_state == 'popup') {
					IKLAD_FUNC.set_cookie("IKLAD.window_open_4524", 1, 30, '/');
					IKLAD_4524.AUTO_CMD_POLLER.stop();
					IKLAD_4524.AUTO_DIE.stop();
					
					//call api
					if ((typeof IKLAD_API_4524 == 'object') && (typeof IKLAD_API_4524.onChatWindowOpen_func == 'function')) {
						IKLAD_API_4524.onChatWindowOpen_func();
					};
				};
				
				
				if (this_state == 'closed') {
					IKLAD_4524.chat_window_open = 0;
					IKLAD_FUNC.delete_cookie("IKLAD.window_open_4524", '/');
					IKLAD_4524.AUTO_CMD_POLLER.start();
					IKLAD_4524.AUTO_DIE.start();
					
					//call api
					if ((typeof IKLAD_API_4524 == 'object') && (typeof IKLAD_API_4524.onChatWindowClose_func == 'function')) {
						IKLAD_API_4524.onChatWindowClose_func();
					};
				};
				
				IKLAD_STATUS_4524.window_state_changed({'state': this_state});
				IKLAD_HINT_4524.window_state_changed({'state': this_state});	//will hide hint box on chat window open
				IKLAD_4524.iframe.contentWindow.postMessage('client_state_data:' + "\n" + JSON.stringify({'chat_window_open': IKLAD_4524.chat_window_open}), '*');	//un-qq!
			},
			
			notify_client_activity: function (params) {
				var obj;
				
				if (params.type == 'client_typing') {
					obj = {
						'type': 'client_typing',
						'status': params.status
					};
				};
				
				if (obj) IKLAD_4524.iframe.contentWindow.postMessage('client_activity:' + "\n" + JSON.stringify(obj), '*');
			},
			
			send_message: function (msg_obj) {
				IKLAD_4524.iframe.contentWindow.postMessage('send_message:' + "\n" + JSON.stringify(msg_obj), '*');
			},
			
			play_sound: function (type) {
				IKLAD_4524.iframe.contentWindow.postMessage('play_sound:' + "\n" + JSON.stringify({'type': type}), '*');
			},
			
			send_opinion: function (id, comment) {
				IKLAD_4524.iframe.contentWindow.postMessage('send_opinion:' + "\n" + JSON.stringify({'id': id, 'comment': comment}), '*');
			},
			
			send_chat_log_to_email: function (email) {
				IKLAD_4524.iframe.contentWindow.postMessage('send_chat_log_to_email:' + "\n" + JSON.stringify({'email': email}), '*');
			},
			
			//user want open chat in new (external) window
			// 2 parameters is REQUIRED:
			//params.height - height of new window
			//params.width - width of new window
			open_in_new_window: function (params) {
				
				var New_win =
				  window.open("https://chat.iklad-chat.biz/ext_win_chat.cgi?c=4524&clientid=" + IKLAD_4524.client_id + "&rnd=" + Math.random(), 
				   "IKLAD_PopupWindow_4524",
				   "menubar=no,location=no,resizable=no,scrollbars=no,status=no,directories=no,height=" + params.height + ",width=" + params.width
				 );
				 
			},
			
			send_offline_form: function (params) {
				IKLAD_4524.iframe.contentWindow.postMessage('send_offline_form:' + "\n" + JSON.stringify(params), '*');
			},
			
			
			get_form_data: function (form_id, msg_id) {
				var params = {
					"form_id": form_id, 
					"msg_id": msg_id
				};
				
				IKLAD_4524.iframe.contentWindow.postMessage('get_form_data:' + "\n" + JSON.stringify(params), '*');
			},
			
			
			send_form_data: function (form_id, msg_id, form_data) {
				var params = {
					"form_id": form_id, 
					"msg_id": msg_id,
					"form_data": form_data
				};
				
				IKLAD_4524.iframe.contentWindow.postMessage('send_form_data:' + "\n" + JSON.stringify(params), '*');
			},
			
			notify_form_completed: function (form_id, msg_id) {
				var params = {
					"form_id": form_id, 
					"msg_id": msg_id
				};
				IKLAD_4524.iframe.contentWindow.postMessage('notify_form_completed:' + "\n" + JSON.stringify(params), '*');
			}
		};
		
		//status JS
		
var IKLAD_STATUS_4524 = {
	TEMPLATE_HTML_CODE: '',	// will hold HTML code for this hint template
	
	TEXT_ONLINE: 'Обменять QIWI на Bitcoin',
	TEXT_OFFLINE: 'Обменник оффлайн',
	
	hide_on_offline: 0,
	hide_on_chat_open: 1,
	
	animated_appearance: 1,
	animation_effect: 'fade_in',
	animation_effect_duration: 200,
	
	animation_effect_step: 0,
	animation_effect_total_steps: 50,
	
	
	curr_op_status: '',
	window_open: false,
	
	first_time_appearance: true,
	i_am_visible: '', //not set
				
	init: function (params) {
		//params.operator_status = 'online' || 'ofline' || ''
		
		var s = document.createElement('div');
		s.innerHTML = IKLAD_STATUS_4524.TEMPLATE_HTML_CODE;
		IKLAD_4524.CODE_CONTAINER.appendChild(s);
		
		IKLAD_STATUS_4524.operator_status_changed(params);
	},
	
	operator_status_changed: function (params) {
		//params.operator_status: 'online' || 'offline' || 'connecting' || 'error' || '' = unknown
		
		//ignore all statuses except 'online' and 'offline'
		if (! ((params.operator_status == 'online') || (params.operator_status == 'offline'))) return;
		
		if (IKLAD_STATUS_4524.curr_op_status == params.operator_status) return;
		
		IKLAD_STATUS_4524.curr_op_status = params.operator_status;
		IKLAD_STATUS_4524.__INT_change_image();
		IKLAD_STATUS_4524.__INT_show_OR_hide_status();
	},
	
	window_state_changed: function (params) {
		//params.state: 'closed' || 'open' | 'popup'
		IKLAD_STATUS_4524.window_open = params.state == 'open';
		IKLAD_STATUS_4524.__INT_show_OR_hide_status();
	},
	
	
	
	//this function is used to retrieve coordinates (POINT with margins) where 'hint box' will be displayed
	// should return object:
	// {
	//  top:					]
	//  left:					] [top || bottom] && [left || right] SHOULD BE DEFINED.
	//  right:				] should end with 'px' or '%'.  Ex: '10px',  '50%'
	//  bottom:				]
	//  position: 'absoulte' || 'fixed'
	//
	//	optional:
	//	margin_top, margin_left, margin_right, margin_bottom   - ONLY IN PIXELS!
	// }
	
	get_hint_box_coords: function () {
		var hint_over_object_container = document.getElementById('IKLAD_STATUS_CONTAINER_WRAP_4524');
		var hint_over_object = document.getElementById('IKLAD_STATUS_CONTAINER_4524');
		
		var res = {};
		
		res.position = 'fixed';
		var browser_size = IKLAD_TEMPLATE_4524.__get_browser_size();
		
		if (hint_over_object_container.style.right) {
			if (hint_over_object_container.style.right.match(/px/)) {
				res.right = parseInt(hint_over_object_container.style.right) + parseInt(hint_over_object_container.offsetWidth/2) + 'px';
			} else {
				res.right = hint_over_object_container.style.right;
				res.margin_right = parseInt(hint_over_object_container.offsetWidth/2);
			};
		};

		if (hint_over_object_container.style.left) {
			if (hint_over_object_container.style.left.match(/px/)) {
				res.left = parseInt(hint_over_object_container.style.left) + parseInt(hint_over_object_container.offsetWidth/2) + 'px';
			} else {
				res.left = hint_over_object_container.style.left;
				res.margin_left = parseInt(hint_over_object_container.offsetWidth/2);
			};
		};

		if (hint_over_object_container.style.top) {
			if (hint_over_object_container.style.top.match(/px/)) {
				res.top = parseInt(hint_over_object_container.style.top) + parseInt(hint_over_object_container.offsetHeight/2) + 'px';
			} else {
				res.top = hint_over_object_container.style.top;
				res.margin_top = parseInt(hint_over_object_container.offsetHeight/2);
			};
		};
		
		if (hint_over_object_container.style.bottom) {
			if (hint_over_object_container.style.bottom.match(/px/)) {
				res.bottom = parseInt(hint_over_object_container.style.bottom) + parseInt(hint_over_object_container.offsetHeight/2) + 'px';
			} else {
				res.bottom = hint_over_object_container.style.bottom;
				res.margin_bottom = parseInt(hint_over_object_container.offsetHeight/2);
			};
		};
		
			
		if (hint_over_object_container.style.marginRight) {
			if (res.margin_right) {
				res.margin_right = parseInt(res.margin_right) + parseInt(hint_over_object_container.style.marginRight) + 'px';
			} else {
				res.margin_right = hint_over_object_container.style.marginRight;
			};
		};

		if (hint_over_object_container.style.marginLeft) {
			if (res.margin_left) {
				res.margin_left = parseInt(res.margin_left) + parseInt(hint_over_object_container.style.marginLeft) + 'px';
			} else {
				res.margin_left = hint_over_object_container.style.marginLeft;
			};
		};
		
		if (hint_over_object_container.style.marginTop) {
			if (res.margin_top) {
				res.margin_top = parseInt(res.margin_top) + parseInt(hint_over_object_container.style.marginTop) + 'px';
			} else {
				res.margin_top = hint_over_object_container.style.marginTop;
			};
		};
		
		if (hint_over_object_container.style.marginBottom) {
			if (res.margin_bottom) {
				res.margin_bottom = parseInt(res.margin_bottom) + parseInt(hint_over_object_container.style.marginBottom) + 'px';
			} else {
				res.margin_bottom = hint_over_object_container.style.marginBottom;
			};
		};
		
		return res;
	},
	
	
	
	
	
	/////////////////////////// INTERNAL FUNCITONS /////////////////////////////////
	
	__INT_change_image: function () {
		var c = document.getElementById('IKLAD_STATUS_CONTAINER_4524');
		var t = document.getElementById('IKLAD_STATUS_TEXT_CONTAINER_4524');
		if (!c) return;
		if (!t) return;
		
		c.style.display = 'none';
		
		if (IKLAD_STATUS_4524.curr_op_status == 'online') {
			c.className = "IKLAD_STATUS_CONTAINER_4524 IKLAD_STATUS_CONTAINER_ONLINE_4524 IKLAD_STATUS_CONTAINER_ONLINE_CUSTOM_4524";
			t.className = "IKLAD_STATUS_TEXT_CONTAINER_ONLINE_4524 IKLAD_STATUS_TEXT_CONTAINER_ONLINE_CUSTOM_4524";
			t.innerHTML = IKLAD_STATUS_4524.TEXT_ONLINE;
		} else {
			c.className = "IKLAD_STATUS_CONTAINER_4524 IKLAD_STATUS_CONTAINER_OFFLINE_4524 IKLAD_STATUS_CONTAINER_OFFLINE_CUSTOM_4524";
			t.className = "IKLAD_STATUS_TEXT_CONTAINER_OFFLINE_4524 IKLAD_STATUS_TEXT_CONTAINER_OFFLINE_CUSTOM_4524";
			t.innerHTML = IKLAD_STATUS_4524.TEXT_OFFLINE;
		};

	},
	
	
	
	__INT_show_OR_hide_status: function () {
		var img_visible = true;
		
		if (IKLAD_STATUS_4524.curr_op_status == 'online') {
			
			if (IKLAD_STATUS_4524.window_open) {
				img_visible = ! IKLAD_STATUS_4524.hide_on_chat_open;
			} else {
				img_visible = true;
			};
			
		} else {		//op OFFLINE
			
			if (IKLAD_STATUS_4524.window_open) {
				img_visible = ! IKLAD_STATUS_4524.hide_on_chat_open;
			} else {
				img_visible = ! IKLAD_STATUS_4524.hide_on_offline;
			};
		};
		
		
		if (img_visible) {
			
			if (IKLAD_STATUS_4524.i_am_visible != '1') {
				IKLAD_STATUS_4524.i_am_visible = '1';
				
				
				
				if (IKLAD_STATUS_4524.first_time_appearance && (IKLAD_STATUS_4524.animated_appearance == 1)) {
					IKLAD_STATUS_4524.first_time_appearance = false;
					IKLAD_STATUS_4524.__INT_appear_animated();
				} else {
					document.getElementById('IKLAD_STATUS_CONTAINER_4524').style.display = '';
				};
				
				
				
			};
			
		} else {
			
			if (IKLAD_STATUS_4524.i_am_visible != '0') {
				IKLAD_STATUS_4524.i_am_visible = '0';
				document.getElementById('IKLAD_STATUS_CONTAINER_4524').style.display = 'none';
			};
			
		};

		
	},
	
	

	__INT_appear_animated: function () {
		
		if (IKLAD_STATUS_4524.animation_effect == 'fade_in') return IKLAD_STATUS_4524.__INT_appear_animated_FADE_IN();
		
		
		
		//unknown animation effect
		document.getElementById('IKLAD_STATUS_CONTAINER_4524').style.display = '';
	},
	
	
	__INT_appear_animated_FADE_IN: function () {
		document.getElementById('IKLAD_STATUS_CONTAINER_4524').style.opacity = 0;
		document.getElementById('IKLAD_STATUS_CONTAINER_4524').style.display = '';
		
		if (typeof jQuery == 'undefined') {
			IKLAD_STATUS_4524.animation_effect_step = 0;
			IKLAD_STATUS_4524.__INT_appear_animated_FADE_IN_STEP();
		} else {
			jQuery('#IKLAD_STATUS_CONTAINER_4524').css({'opacity': 0}).animate({'opacity': 1}, {'duration': IKLAD_STATUS_4524.animation_effect_duration});
		};
	},
	
	__INT_appear_animated_FADE_IN_STEP: function () {
		IKLAD_STATUS_4524.animation_effect_step++;
		
		if (IKLAD_STATUS_4524.animation_effect_step >= IKLAD_STATUS_4524.animation_effect_total_steps) {
			document.getElementById('IKLAD_STATUS_CONTAINER_4524').style.opacity = 1;
			return;
		};
		
		var opc = IKLAD_STATUS_4524.animation_effect_step / IKLAD_STATUS_4524.animation_effect_total_steps;
		document.getElementById('IKLAD_STATUS_CONTAINER_4524').style.opacity = opc;
		
		setTimeout(IKLAD_STATUS_4524.__INT_appear_animated_FADE_IN_STEP, Math.round(IKLAD_STATUS_4524.animation_effect_duration / IKLAD_STATUS_4524.animation_effect_total_steps));
	},
	



	
	
	
	
	
	last_element_for_IE: ''
};

		IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '<style type="text/css">';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	#IKLAD_STATUS_CONTAINER_4524, #IKLAD_STATUS_TEXT_CONTAINER_4524, #IKLAD_STATUS_CONTAINER_TBL_4524 {';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		display: block;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		box-sizing: border-box;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		outline: none;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		width: auto;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		min-width: 0;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		max-width: none;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		height: auto;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		min-height: 0;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		max-height: none;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		text-indent: 0;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		line-height: normal;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		text-decoration: none;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		padding: 0;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		border: none;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	}';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	#IKLAD_STATUS_CONTAINER_TBL_4524 * {';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		outline: none;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		width: auto;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		min-width: 0;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		max-width: none;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		height: auto;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		min-height: 0;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		max-height: none;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		border: none;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		background: none;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		padding: 0;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		margin: 0;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	}';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	#IKLAD_STATUS_CONTAINER_WRAP_4524 {';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		position: fixed; ';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		z-index:2100000000; ';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	}';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	#IKLAD_STATUS_CONTAINER_4524 {';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		position: relative;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		left:0; bottom:0; ';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		 ';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		 ';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		margin-bottom:0px; ';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		margin-left:0px; ';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '			border-top-left-radius: 5px;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '			border-top-right-radius: 5px;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		cursor: pointer;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		text-align: center;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '				';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '			';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '				';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	}';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	#IKLAD_STATUS_TEXT_CONTAINER_4524 {';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		font-size: 22px;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		font-weight: normal;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		font-family: "Verdana Cyr",Verdana,"Arial Cyr",Arial,"Helvetica Cyr",Helvetica,sans-serif;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		white-space: nowrap;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		text-shadow: 1px 1px 2px #000000;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	}';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	#IKLAD_STATUS_CONTAINER_TBL_4524 {';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		padding: 1px 12px 1px 10px;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		border: 0;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	}';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	.IKLAD_STATUS_CONTAINER_ONLINE_4524 {';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		background: #BF2121;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		border: 1px solid #661111;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	}';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	.IKLAD_STATUS_TEXT_CONTAINER_ONLINE_4524 {';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		color: #FFFFFF;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	}';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	.IKLAD_STATUS_CONTAINER_OFFLINE_4524 {';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		background: #BF2121;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		border: 1px solid #661111;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	}';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	.IKLAD_STATUS_TEXT_CONTAINER_OFFLINE_4524 {';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		color: #FFFFFF;';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	}';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	/* online class,  use "!important" to override styles */';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '.IKLAD_STATUS_CONTAINER_ONLINE_CUSTOM_4524 {';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '}';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '.IKLAD_STATUS_TEXT_CONTAINER_ONLINE_CUSTOM_4524 {';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '}';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '/* offline class, use "!important" to override styles */';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '.IKLAD_STATUS_CONTAINER_OFFLINE_CUSTOM_4524 {';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '}';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '.IKLAD_STATUS_TEXT_CONTAINER_OFFLINE_CUSTOM_4524 {';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '}';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '</style>';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '<div id="IKLAD_STATUS_CONTAINER_WRAP_4524" style="left:0; bottom:0;  ">';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	<div id="IKLAD_STATUS_CONTAINER_4524" class="IKLAD_STATUS_CONTAINER_4524" onclick="IKLAD_TEMPLATE_4524.open_chat_window()" style=" width: 330px;  height: 35px; ">';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		<table cellpadding=0 cellspacing=0 id="IKLAD_STATUS_CONTAINER_TBL_4524">';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '			<tr>';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '				<td style="vertical-align: bottom; padding-right: 4px;  " id="IKLAD_STATUS_CONTAINER_ICON_IMG_4524">';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '					<img style="border: 0; margin:0 padding: 0;" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyZpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTExIDc5LjE1ODMyNSwgMjAxNS8wOS8xMC0wMToxMDoyMCAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTUgKFdpbmRvd3MpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjgxQzhFRDJGMEM2NDExRTZCNjQzQ0FCNTJENjFCOUJFIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjgxQzhFRDMwMEM2NDExRTZCNjQzQ0FCNTJENjFCOUJFIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6ODFDOEVEMkQwQzY0MTFFNkI2NDNDQUI1MkQ2MUI5QkUiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6ODFDOEVEMkUwQzY0MTFFNkI2NDNDQUI1MkQ2MUI5QkUiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz7QI2JLAAABeklEQVR42mJkwA9UgVgLiCWh/JdAfB2IbzCQCIKAeCMQ/wLi/2j4LxBvA+JIYgwyAeKzaAbcBOJdQLwT6jpkuWtAbIvLsGgkhSCNSUAsikWdEBDHAvF5JPXp6IqckCRbSAiaciR9gTBBJiD+BhUsYyAdpEH1/gFiHpBALlRgLwP5YDPUjFYQ5xyU44ikwABNgwIUM+BQYwo14z4DUhgIQCUnQPkJUD5I/AMQP0BSUwBVMwHJ0N8gMSYkga9Q+gMWF4AMk0cy8AOSZTDwB8Z4AbVNBUkyAIv30IPBAclAKagZn0Cc2VBOIwWRUgs1Yy0sv8LC0YAMwySA+Ae6/n7kWCIBSAPxE6jeucgShlDBs0QaxALEWUD8D6rvALIELOvBXAoL8Hog/gnEJ6Cu+Af1HshbPkDMCVU7H5rvUcBhpHS1F0uRhQ3vA2I3dIMYoaXHWzTxU0DcDnWVEdRloDT7BlpkHcUX3mugNh6GRr8uA4UgEYhtGKgEAAIMAN8UdsDgdn3qAAAAAElFTkSuQmCC">';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '				</td>';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '				';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '				<td id="IKLAD_STATUS_TEXT_CONTAINER_4524">';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '					';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '				</td>';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '			</tr>';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		</table>';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '	</div>';
IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_STATUS_4524.TEMPLATE_HTML_CODE += '</div>';


		//hint template
		
var IKLAD_HINT_4524 = {
	TEMPLATE_HTML_CODE: '',	// will hold HTML code for this hint template
	
	hint_container: '',
	hint_text_container: '',
	
	init: function () {		
		var d = document.createElement('div');
		d.setAttribute("style", "position: absolute;");
		d.style.position = 'absolute';
		d.style.top = '0px';
		d.style.left = '0px';
		d.innerHTML = IKLAD_HINT_4524.TEMPLATE_HTML_CODE;
		document.body.appendChild(d);
		
		IKLAD_HINT_4524.hint_container = document.getElementById('IKLAD_HINT_CONTAINER_4524');
		IKLAD_HINT_4524.hint_text_container = document.getElementById('IKLAD_HINT_TEXT_CONTAINER_4524');
	},
	
	window_state_changed: function (params) {
		//params.state: 'closed' || 'open' | 'popup'
		
		//process only 'open' state
		if (params.state == 'open') {
			IKLAD_HINT_4524.hide();
		};
		
	},
	
	show: function (msg_text, show_point) {
		if (! IKLAD_HINT_4524.hint_container) return;
		if (! IKLAD_HINT_4524.hint_text_container) return;
		
		IKLAD_HINT_4524.hint_text_container.innerHTML = msg_text;
		
		var hint_container = IKLAD_HINT_4524.hint_container;
		 
		var positionClass_1;
		var positionClass_2;
		var hint_container_Width = 248;
		var hint_container_Height = 207;
		
		hint_container.style.position = show_point.position;
		
		
		hint_container.style.display = 'none';	
		hint_container.style.top = null;
		hint_container.style.bottom = null;
		hint_container.style.right = null;
		hint_container.style.left = null;
		
		hint_container.style.marginTop = null;
		hint_container.style.marginBottom = null;
		hint_container.style.marginLeft = null;
		hint_container.style.marginRight = null;
		
		
		if (show_point.position == 'absoulte') {

			
			/*
			var trueBody = (document.compatMode && document.compatMode!="BackCompat")? document.documentElement : document.body;
			
      if ( parseInt(trueBody.clientWidth + trueBody.scrollLeft) < parseInt(hint_container_Width + Pos[0])) {
        positionClass = "IKLAD_Right";
        Pos[0] -= hint_container_Width;
      } else {
	      positionClass = "IKLAD_Left";
      };
      
      if ( parseInt(trueBody.clientHeight + trueBody.scrollTop) < parseInt(hint_container_Height + Pos[1])) {
        positionClass += "Bottom";
        Pos[1] -= hint_container_Height;
      } else {
        positionClass += "Top";
      };
      
      */
		};
		
	
		var browser_size = IKLAD_HINT_4524.__get_browser_size();
		
		var corner_left_right = '';
		var corner_top_bottom = '';
		
		if (show_point.left) {
			hint_container.style.left = show_point.left;
			
			if (show_point.left.match(/px/)) {
				corner_left_right = (parseInt(show_point.left) <= (browser_size.width/2)) ? 'left' : 'right';
			} else {
				corner_left_right = (parseInt(show_point.left) <= 50) ? 'left' : 'right';
			};
		};
		
		if (show_point.right) {
			hint_container.style.right = show_point.right;
			
			if (show_point.right.match(/px/)) {
				corner_left_right = (parseInt(show_point.right) <= (browser_size.width/2)) ? 'right' : 'left';
			} else {
				corner_left_right = (parseInt(show_point.right) <= 50) ? 'right' : 'left';
			};
		};
		
		if (show_point.top) {
			hint_container.style.top = show_point.top;
			
			if (show_point.top.match(/px/)) {
				corner_top_bottom = (parseInt(show_point.top) <= (browser_size.height/2)) ? 'top' : 'bottom';
			} else {
				corner_top_bottom = (parseInt(show_point.top) <= 50) ? 'top' : 'bottom';
			};
		};
		
		if (show_point.bottom) {
			hint_container.style.bottom = show_point.bottom;
			
			if (show_point.bottom.match(/px/)) {
				corner_top_bottom = (parseInt(show_point.bottom) <= (browser_size.height/2)) ? 'bottom' : 'top';
			} else {
				corner_top_bottom = (parseInt(show_point.bottom) <= 50) ? 'bottom' : 'top';
			};
		};
		
		
		
		show_point.margin_left = parseInt(typeof show_point.margin_left != 'undefined' ? show_point.margin_left : 0);
		show_point.margin_right = parseInt(typeof show_point.margin_right != 'undefined' ? show_point.margin_right : 0);
		show_point.margin_top = parseInt(typeof show_point.margin_top != 'undefined' ? show_point.margin_top : 0);
		show_point.margin_bottom = parseInt(typeof show_point.margin_bottom != 'undefined' ? show_point.margin_bottom : 0);
		
		
		if (corner_left_right == 'left') {
			positionClass_1 = "IKLAD_Left";
			
			if (show_point.left) {
				hint_container.style.marginLeft = show_point.margin_left + 'px';
			} else {
				hint_container.style.marginRight = -(hint_container_Width - show_point.margin_right) + 'px';
			};
			
		} else {
			positionClass_1 = "IKLAD_Right";
			
			if (show_point.left) {
				hint_container.style.marginLeft = -(hint_container_Width - show_point.margin_left) + 'px';
			} else {
				hint_container.style.marginRight = show_point.margin_right + 'px';
			};

		};
		
		
		if (corner_top_bottom == 'top') {
			positionClass_2 = "Top";
			
			if (show_point.top) {
				hint_container.style.marginTop = show_point.margin_top + 'px';
			} else {
				hint_container.style.marginBottom = -(hint_container_Height - show_point.margin_bottom) + 'px';
			};
			
		} else {
			positionClass_2 = "Bottom";
			
			if (show_point.top) {
				hint_container.style.marginTop = -(hint_container_Height - show_point.margin_top) + 'px';
			} else {
				hint_container.style.marginBottom = show_point.margin_bottom + 'px';
			};

		};
						
		
		hint_container.className = positionClass_1 + positionClass_2 + '_4524';
		hint_container.style.display = '';
	},
	
	
	hide: function (event) {
		if (! IKLAD_HINT_4524.hint_container) return;
		IKLAD_HINT_4524.hint_container.style.display = 'none';
		
		try { event.stopPropagation(); event.cancelBubble = true; } catch (r) {};
	},
	
	
	
	
	
	
	
	
	/////////////// INTERNAL FUNC ///////////////
	
	__my_open_chat: function () {
		IKLAD_HINT_4524.hide(); 
		IKLAD_TEMPLATE_4524.open_chat_window();
	},
	
	__get_browser_size: function () {
		var e = window, a = 'inner';
		if ( !( 'innerWidth' in window ) ) {
			a = 'client';
			e = document.documentElement || document.body;
		};
		return { width : e[ a+'Width' ] , height : e[ a+'Height' ] }
	}
};
		IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '<style type="text/css">';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '	div.IKLAD_RightBottom_4524 {';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '		background: url(https://chat.iklad-chat.biz/img/hint_template/0/rb.png) no-repeat;';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '	}';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '	div.IKLAD_RightTop_4524 {';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '		background: url(https://chat.iklad-chat.biz/img/hint_template/0/rt.png) no-repeat;';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '	}';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '	div.IKLAD_LeftBottom_4524 {';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '		background: url(https://chat.iklad-chat.biz/img/hint_template/0/lb.png) no-repeat;';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '	}';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '	div.IKLAD_LeftTop_4524 {';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '		background: url(https://chat.iklad-chat.biz/img/hint_template/0/lt.png) no-repeat;';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '	}';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '	';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '	div.IKLAD_HINT_BTN_4524 {';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '		border: 1px solid lightgray; ';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '	  color: gray; ';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '	  cursor: pointer;';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '	  padding: 3px 5px;';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '	  float: left;';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '	  font-size: 12px;';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '	}';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '	';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '	#IKLAD_HINT_CONTAINER_4524 {';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '		border: 0; ';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '		margin: 0; ';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '		padding: 0; ';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '		text-align: left;';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '		z-index: 2100000100;';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '		';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '	}';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '</style>';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '<div id="IKLAD_HINT_CONTAINER_4524" style="display: none; position: absolute;">';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '	<div style="width: 248px; height: 207px; margin: 0; padding: 0; text-align: left;">';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '		<div onclick="IKLAD_HINT_4524.__my_open_chat();" style="cursor: pointer; position: relative; width: 200px; height: 148px; overflow: auto; text-align: left; margin: 0; padding: 5px; top: 23px; left: 18px;">';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '		  ';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '			<div style="float: right; border: 1px solid lightgray; padding: 0px 3px; color: lightgray; cursor: pointer; margin-left: 1px; margin-bottom: 5px; display: none;" id="IKLAD_HINT_CLOSE_BTN_X_4524" onclick="IKLAD_HINT_4524.hide(event);" title="&#67;&#108;&#111;&#115;&#101;">X</div>';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '			';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '			<span id="IKLAD_HINT_TEXT_CONTAINER_4524" style=" color: black; font-size: 14px;"></span>';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '			';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '			<div style="position: absolute; bottom:0; width: 190px;">';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '       <table style="margin: 0 auto;">';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '        <tr>';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '          <td>';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '      			<div style="" class="IKLAD_HINT_BTN_4524" id="IKLAD_HINT_START_CHAT_BTN_4524" onclick="IKLAD_HINT_4524.__my_open_chat();">&#83;&#116;&#97;&#114;&#116;&#32;&#99;&#104;&#97;&#116;</div>';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '					  <div style="margin-left: 5px; " class="IKLAD_HINT_BTN_4524" id="IKLAD_HINT_CLOSE_BTN_4524" onclick="IKLAD_HINT_4524.hide(event);">&#67;&#108;&#111;&#115;&#101;</div>';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '          </td>';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '          ';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '        </tr>';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '       </table>';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '			</div>';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '	</div>';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";IKLAD_HINT_4524.TEMPLATE_HTML_CODE += '</div>';
IKLAD_HINT_4524.TEMPLATE_HTML_CODE += "\n";
		
		//form JS
		var IKLAD_NEED_JQUERY_4524 = 0;
var IKLAD_NEED_JQUERY_UI_4524 = 0;


<!-- we need this for form show/hide animation -->
	IKLAD_NEED_JQUERY_4524 = 1;






if ((typeof jQuery == 'undefined') && (IKLAD_NEED_JQUERY_4524 == 1)) {
	var s = document.createElement('script');
	s.type = 'text/javascript';
	s.charset = 'utf-8';
	s.src = 'https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js';

	if (IKLAD_NEED_JQUERY_UI_4524 == 1) {
		s.onload = function () {
			var s_ui = document.createElement('script');
			s_ui.type = 'text/javascript';
			s_ui.charset = 'utf-8';
			s_ui.src = 'https://code.jquery.com/ui/1.11.2/jquery-ui.min.js';
			document.body.appendChild(s_ui);
		};
	};

	document.body.appendChild(s);
};




var IKLAD_TEMPLATE_4524 = {
	//mandatory functions
	curr_operator_status: '',
	__offline_actions: [],
	
	init: function (params) {
		//params.operator_status = 'online' || 'offline'
		
		//params.opinions :  array of objects:
		// {
		//  id: id of opinion
		//  text: text to diaply
		//	want_comment: 1|0  whether or not ask user for comments when choosing this variant
		// }, ... {}, {} ...

		
		//init 'messages' iframe
		var fr = window.frames.IKLAD_MSGS_IFR_4524;
		var d = fr.document;
		d.open();
		d.write('<html><head><META HTTP-EQUIV="Pragma" CONTENT="No-Cache"><META HTTP-EQUIV="CACHE-CONTROL" CONTENT="NO-CACHE"><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><base target="_Blank"></head>');
		d.write('<body leftmargin="0" topmargin="0" rightmargin="0" bottommargin="0" marginwidth="0" marginheight="0">');
		
		d.write('	\
			<style type="text/css"> \
			::-webkit-scrollbar {	\
				width: 12px;	\
			}	\
			::-webkit-scrollbar-track {	\
				background-color: #ebf1f8;	\
			}	\
			::-webkit-scrollbar-thumb {	\
				background-color: #abb7c8;	\
			}	\
			table { \
				padding: 0; \
				margin: 0; \
				border-collapse: collapse; \
				border-spacing: 0; \
			} \
			div.msg_line { \
				margin: 4px 0 7px 0; \
				width: 100%; \
				box-sizing: border-box; \
			} \
			div.msg_line_form { \
				padding: 0 30px 0 8px; \
			}\
			td.msg_from_operator_left { \
				width: 10px; \
				background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAPCAYAAADZCo4zAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAANhJREFUeNp0kN1ugzAMhU8cQsi0qXv/h+rdHmCTWgoRHeGfBvA6LipFgCXf+Hy2jw6YGXvtveevnzMTDspPHloaiH96r1xVcjkUOLzQDg0Wmo6BundQcbQPdH3HQgLiqW48POaRL/k3WM3QSRwC0+I5qy5wzR2nz9M6C4Df1nLmrjBvBlEkQ8AWORdthuQjhlLRa0mktyvXgwNphnlPwFgCT8RqwqI8pKaN+Hpxry1bdwMpIDEGRCIE1uznB+dliqKyT5Masdar0U0OzejYVin6sQNJiT8BBgAr55BAcCyxhAAAAABJRU5ErkJggg=="); \
				background-repeat: no-repeat; \
				background-position: 3px 50%; \
			} \
			div.msg_from_operator { \
				border-radius: 6px;	\
				background: #e4f3dc;	\
				border: 1px solid #d4e3cd;	\
				font-size: 12px; \
				padding: 7px 7px 7px 7px; \
				font-family: Tahoma; \
				word-wrap: break-word; \
				word-break: break-all; \
			}	\
			td.msg_from_operator_time { \
				width: 30px; \
				text-align: center; \
				color: #c7c7c7; \
				font-size: 10px; \
			} \
			td.msg_from_client_right { \
				width: 10px; \
				background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAPCAYAAADZCo4zAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAALFJREFUeNp0kb0OhCAQhAfBBFETfP/Hs9LCghh/UY6xMJc7mGQp2C/L7IC+78N5niEKqSqklPDeI6eiLEscx5EHlFLY9z0PGGOwLEseiAKnrOsakgCPpmngnEMWqOsa13VhnueQBKiu6whg27aQBLhu27YYxxHTNL2QYIq/YyNA09BaQ6WM0dN93/8AL7kNg6OnmJF4noj1hMWmtZZN8XoYhiHws6qqekzG0MT31I8AAwAe8WscLh05SgAAAABJRU5ErkJggg=="); \
				background-repeat: no-repeat; \
				background-position: -1px 50%; \
			} \
			div.msg_from_client { \
				border-radius: 6px;	\
				background: #fbfbfb;	\
				border: 1px solid #e1e1e1;	\
				font-size: 12px; \
				padding: 7px 7px 7px 7px; \
				font-family: Tahoma; \
				word-wrap: break-word; \
				word-break: break-all; \
			}	\
			td.msg_from_client_time { \
				width: 30px; \
				text-align: center; \
				color: #c7c7c7; \
				font-size: 10px; \
			} \
			</style>	\
		');
		
		d.write('<div id="MSGS_CONTAINER"></div>');
		d.write('<div id="OPERATOR_TYPING_CONTAINER" style="display: none; opacity: 0.5; padding-left: 3px;">	\
			<table width=100% cellpadding=0 cellspacing=0><tr> \
			<td class="msg_from_operator_left"></td> \
			<td class="msg_from_operator"><div class="msg_from_operator" id="OPERATOR_TYPING_MSG" style="font-size: 11px;"></div></td> \
			<td class="msg_from_operator_time">&nbsp;</td> \
			</tr></table></div>');
		d.write('</bo' + 'dy></ht' + 'ml>');
		d.close();
		
		IKLAD_TEMPLATE_4524.msgs_ifr = fr;
		IKLAD_TEMPLATE_4524.msgs_container = d.getElementById('MSGS_CONTAINER');
		
		//here NOT d. , but DOCUMENT 
		IKLAD_TEMPLATE_4524.top_form_container_tr = document.getElementById('TOP_FORM_CONTAINER_TR');
		IKLAD_TEMPLATE_4524.top_form_container = document.getElementById('TOP_FORM_CONTAINER');
		IKLAD_TEMPLATE_4524.bottom_form_container_tr = document.getElementById('BOTTOM_FORM_CONTAINER_TR');
		IKLAD_TEMPLATE_4524.bottom_form_container = document.getElementById('BOTTOM_FORM_CONTAINER');
		
		IKLAD_TEMPLATE_4524.operator_typing_container = d.getElementById('OPERATOR_TYPING_CONTAINER');
		IKLAD_TEMPLATE_4524.operator_typing_msg_container = d.getElementById('OPERATOR_TYPING_MSG');
		
		IKLAD_TEMPLATE_4524.__iframe_import_CSS();
		
		//init 'leave opinion dialog'
		var opinions_html_code = '<table cellpadding=0 cellspacing=0 style="margin: 0; padding: 0;">';
		opinions_html_code += '<tr id="IKLAD_OPINION_HEADER_4524"><td>Оставить отзыв</td><td width=10 style="padding: 0 1px 0 5px !important;" align=center><a style="text-decoration: none;" href="#" onclick="IKLAD_TEMPLATE_4524.local_hide_opinion_dialog(); return false;" title="закрыть">x</a></td></tr>';

		for (var i=0; i < params.opinions.length; i++) {
			opinions_html_code += '<tr>';
			opinions_html_code += '<td colspan=2 class="IKLAD_OPINION_LIST_4524" onclick="javascript:IKLAD_TEMPLATE_4524.local_opinion_set(' + params.opinions[i].id + ',' + params.opinions[i].want_comment + ')">' + params.opinions[i].text + '</td>';
			opinions_html_code += '</tr>';
		};

		opinions_html_code += '</table>';

		var dv = document.createElement('div');
		dv.setAttribute('id', 'IKLAD_OPINION_BOX_4524');
		dv.setAttribute('style', 'z-index: 100000000000;');
		dv.style.zIndex = 100000000000;
		dv.innerHTML = opinions_html_code;
		dv.style.display = 'none';
		document.body.appendChild(dv);
		
		IKLAD_TEMPLATE_4524.original_form_height = document.getElementById('IKLAD_SET_HEIGHT_TD_4524').style.height;
	},
	
	
	//	
	__iframe_import_CSS: function () {
		var fr = IKLAD_TEMPLATE_4524.msgs_ifr;
		var css = document.getElementById('IKLAD_CSS_4524');
		if (! css) return;
		
    var st = fr.document.createElement("style");
    st.type = "text/css";
    try {
     st.innerHTML = css.innerText;
    } catch (ex) {
     st.styleSheet.cssText = css.innerText;  // IE8 and earlier
    };
    
    fr.document.getElementsByTagName("head")[0].appendChild(st);
	},
	
	operator_status_changed: function (params) {
		//params.operator_status = 'online' || 'offline' || 'connecting' || 'error' | 'no_empty_accounts'
		
		//--- params.operator_status == 'online' || 'offline'
		//>>>no additional params		
		
		//--- params.operator_status == 'offline'
		//>>> params.actions = [			// list of actions to do
		//>>>   {
		//>>>   	action: 'form' | 'message'
		//>>>   	param: 'form_ID' | 'message_text'
		//>>>   }
		//>>> ]
		
		//--- params.operator_status == 'connecting' || 'no_empty_accounts'
		//>>> no additional params
		
		//--- params.operator_status == 'error'
		//>>> params.error_message => text error
		
		var img_el = document.getElementById('IKLAD_OP_STATUS_IMG_4524');
		var text_el = document.getElementById('IKLAD_OP_STATUS_TEXT_4524');
		
		var __onl = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAASVJREFUeNpUkr1twzAUhBmBa2QKVenSyZ2KzOE6M3gFT5BGhUt16Vy5yAzaQeTjexRyxx/EMXAwKH13fO+gl+vPl2u/V+gDmvSwMWV1ktNDTNY9yxI1bsGi8w1+gz6hWbM5PQoMySnkeAom74Avu8a7b8kFtsNc6rAlB9CFDGmcgwWc49m3MWYlnJ/h6HYoNO0qM87fNExM1uM/TMVu0tDNkzcuCDgaYWljMLHCex2lBcjoBWMkJONQEmkoYH6CYeYuZAZWRyjmuiChXat6Mp/zdrIDe6aTKX0MjlRSS3pN5n6adR3gXvDiVq/ncrgl/ZkkVxgN3tDk4vFwA3wJNX3uI9QxU08mfEGjm691yR3/Z/bM6mAeCSeTRzpsRZMLYX4SvwIMAMzxjYuV11bYAAAAAElFTkSuQmCC';
		var __ofl = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAXhJREFUeNpUkk1KA0EQhWuaCfkFTQxmlm7MFRTJIbyEd8gqi6xyB5e5yqBk40IUEYRANBBG0xqwf6p6krFrZgKmoWgYvvfqVfUE6+kU+Lyeiou6g2ELs0FdUSdFB2uBUgYUS7CT/stmRlpByPBbV9ycqGzcVVmUOgdbJAgI4ciYbt3o612VLh966ej8Sd+G7HwAE4FDBLIGyGggZeD4S0ebOo7vz7JHwTEY3no4ZdhaXyWsDaDWgEpBe7GJKvJ3GHLm/3DqizxExsOKRSoX8Ldakg7CfECf11nMBQy6A7joxNVUthOm5CBAKmN4gQfQFI5UOqMuIvrJQKwDlOxK2mcvXXORLqroqH1Z+GxspZBAcTGcAruHOMp+Dr55EWghae5iIYWdvFdxtQc5BvpVOlWIiq0hzHvBSjayieg//8yWVRwtGrSifx3yKOXW5j1YLbtidHW3mYUM8Avyo3xEu2EtcYOG3xz5EZP2TiatSvztnRnmv+JPgAEARo90fEfRwVgAAAAASUVORK5CYII=';
		var __loading = 'data:image/gif;base64,R0lGODlhEAAQAMQAAP////f39+/v7+fn59/f39fX187OzsbGxr6+vra2trKysq6urqqqqp6enpaWlpKSko6OjoqKioaGhoKCgnV1dW1tbWVlZV1dXVVVVU1NTT09PTU1NS0tLSQkJCAgIBwcHCH/C05FVFNDQVBFMi4wAwEAAAAh+QQJCgAAACwAAAAADgAOAAAFOyAgjkBVkWQAideFktbaisE7YIPl1mPSCICGQjBIiRIOxAvAEwkMS9FgCowCplOrNtpENbsvcBdMC4tCACH5BAkKAAAALAAAAAAOAA4AAAU6ICCOgOOQZJCIUSRaBNqsLUBxKBA4AQQNHcRoUBAhDILdRRQQEQc5HUoQrVqvWGszupVqUV0vOLcNAQAh+QQJCgAAACwCAAAADQAOAAAFOyAgiggynsAgJokICSehskBjoUABJIhw6QBBQDSA7SQAAwcDGOIsn4oTB4AYqNisFjtFObu4rjhMFoUAACH5BAkKAAAALAIAAAAOAA4AAAU7ICCKwzCeaCkmAdoC6tGgYlsGjgm071kkAIJlUqMBIBiH8ZQQLE+CyuVSeQ4s0+rTtez1jN/dKVzkjkIAIfkECQoAAAAsAgABAA4ADQAABTcgII7jQIrBORAnShZjmp6BKTSK2yIO0p4Gwe8kcEQijiEgYEQqHabYD9OZ6H6IzYU0uwqv0lEIACH5BAkKAAAALAIAAgAOAA0AAAU3IAAEYjmaJZmuKloSg9iaQxG75oyLApIkiJ3IBxQqZjpR5NKQuSAWQKECyZUKnwNvZapohN1WCAAh+QQJCgAAACwCAAIADgAOAAAFOSAABGI5miWZoiq6ii3rzrQ73EMNCHhtyK6E4wAzGQoJCGDASJhImIvgUnCpLheAo1LDihy1CtcVAgAh+QQJCgAAACwCAAIADQAOAAAFOCAABGI5miJZqimKquzrznRt24IZl0ORqxXIoJcQEQaiwqcAiQAcOdPmAog4EQxdhWQVIWgOhysEACH5BAkKAAAALAAAAgAOAA4AAAU4ICACwTiWpoiq6Zqy8Ou+dG3f4uDg0ZfRqMsmAXAwAgMka5DDDBDEAs0CASSIA0LLUbrmbAhEKgQAIfkECQoAAAAsAAACAA4ADgAABTogIALBOJamiKrpmrLw675pdV1WQYv2VQ27VCIoYmAmNNSjYgAgmi0AUOoYWEm0xvCKNQUQJS5RLAoBACH5BAkKAAAALAAAAgAOAA0AAAU4ICACwTiWIkqaKnBxhSmXguVVcmoWTz46kYejJQMGB75cLCk6OBQ+VKKBHAhyxKUuR0CyZgPiKAQAIfkECQoAAAAsAAABAA4ADQAABTkgIApXIJ7ouV2pKbrFZ5yuKFkDQEkpYAYQjKPnQxEWRBEikUAklUxE7VmkCgoEomuQfU6rL23PFQIAOw==';

		if (params.operator_status == 'connecting') {
			img_el.src = __loading;
			text_el.innerHTML = 'подключение';
		};
	
		if (params.operator_status == 'online') {
			img_el.src = __onl;
			text_el.innerHTML = 'онлайн';
		};
		
		if (params.operator_status == 'offline') {
			img_el.src = __ofl;
			text_el.innerHTML = 'оффлайн';
		};
		
		if (params.operator_status == 'no_empty_accounts') {
			img_el.src = __ofl;
			text_el.innerHTML = 'нет свободных каналов';
		};
		
		if (params.operator_status == 'error') {
			img_el.src = __ofl;
			text_el.innerHTML = 'ошибка соединения с оператором';
		};
		
		
		//////////
		var online_offline_op_status;
		
		if (! ((params.operator_status == 'online') || (params.operator_status == 'offline')) ) {
			return; // NO FUTHER procrssing of statuses. only online and offline
		};
		
		if (IKLAD_TEMPLATE_4524.curr_operator_status == params.operator_status) return;
		IKLAD_TEMPLATE_4524.curr_operator_status = params.operator_status;
		
		if (params.operator_status == 'online') {
			IKLAD_TEMPLATE_4524.__show_layer('online');
		}; 

		if (params.operator_status == 'offline') {
			IKLAD_TEMPLATE_4524.__offline_actions = params.actions;
			IKLAD_TEMPLATE_4524.__show_layer('offline');
		}; 
	},
	
	
	__show_layer: function (layer) {
		
		if (layer == 'default') {
			if (IKLAD_TEMPLATE_4524.curr_operator_status == 'online') {
				layer = 'online';
			};
			
			if (IKLAD_TEMPLATE_4524.curr_operator_status == 'offline') {
				layer = 'offline';
			};
		};
		
		//for state 'connecting', etc, .
		if (layer == 'default') {
			layer = 'loading';
		};
				
		
		var loading_layer_visible = false;
		var modal_layer_visible = false;
		var online_layer_visible = false;
		var footer_visible = false;
		var textarea_visible = false;
		
		var reset_from_height = false;
		var set_original_from_height = true;
		
		if (layer == 'online') {
			online_layer_visible = true;
			footer_visible = true;
			textarea_visible = true;
		};
	
		if (layer == 'loading') {
			loading_layer_visible = true;
		};
		
		if (layer == 'modal_form') {
			modal_layer_visible = true;
			reset_from_height = true;
		};
	
	
		if (layer == 'offline') {
			
			for (var i=0; i < IKLAD_TEMPLATE_4524.__offline_actions.length; i++) {
				var this_action = IKLAD_TEMPLATE_4524.__offline_actions[i];
				
				if (this_action.action == 'form') {
					IKLAD_TEMPLATE_4524.local_on_chat_message({
						"type": 'form',
						"text": this_action.param, 
						"to": "client", 
						"dt": "",
						"id": 0,
						"is_info": 1,
						"by_human": 0
					});
					continue;
				};
				
				
				if (this_action.action == 'message') {
					online_layer_visible = true;
					
					IKLAD_TEMPLATE_4524.local_on_chat_message({
						"type": 'msg',
						"text": this_action.param, 
						"to": "client", 
						"dt": "", 
						"id": 0, 
						"is_info": 1,
						"by_human": 0
					});
					
					continue;
				};
			};
			
		};
	
	
		document.getElementById('LOADING_LAYER_4524').style.display = loading_layer_visible ? '' : 'none';
		document.getElementById('MODAL_FORM_LAYER_4524').style.display = modal_layer_visible ? '' : 'none';
		document.getElementById('ONLINE_LAYER_4524').style.display = online_layer_visible ? '' : 'none';
		
		document.getElementById('IKLAD_TEXTAREA_ROW_CONTAINER_4524').style.display = textarea_visible ? '' : 'none';
		//document.getElementById('IKLAD_FOOTER_4524').style.display = footer_visible ? '' : 'none';
		
		if (reset_from_height) {
			document.getElementById('IKLAD_SET_HEIGHT_TD_4524').style.height = null;
		};
		
		if (set_original_from_height && (! reset_from_height)) {
			document.getElementById('IKLAD_SET_HEIGHT_TD_4524').style.height = IKLAD_TEMPLATE_4524.original_form_height;
		};
	},
	
	
	operator_data_changed: function (params) {
		//params.name - name of currently assigned operator
		//params.photo - abs path to image
		
		if (typeof params.photo != 'undefined') {
			document.getElementById('IKLAD_OPERATOR_PHOTO_4524').src = params.photo;
		};
	},
	
	
	operator_activity: function (params) {
		//params.type == 'operator_typing'			- operator keyboard activity
		//params.status = 'composing' || 'paused' || ''				('' = clear status)
		
		if (params.type == 'operator_typing') {
			
			if (params.status == '') {
				IKLAD_TEMPLATE_4524.operator_typing_container.style.display = 'none';
				IKLAD_TEMPLATE_4524.operator_typing_msg_container.innerHTML = '';
			};
			
			if (params.status == 'paused') {
				IKLAD_TEMPLATE_4524.operator_typing_container.style.display = '';
				IKLAD_TEMPLATE_4524.operator_typing_msg_container.innerHTML = 'оператор приостановил печать ...';
			};
			
			if (params.status == 'composing') {
				IKLAD_TEMPLATE_4524.operator_typing_container.style.display = '';
				IKLAD_TEMPLATE_4524.operator_typing_msg_container.innerHTML = '<img src="//chat.iklad-chat.biz/img/templates/design3/composing.gif" style="padding-right:4px;">оператор печатает ...';
			};
			
			IKLAD_TEMPLATE_4524.scrol_msg_list_to_bottom();
		};
		
	},
	
	open_chat_window: function (params) {
		IKLAD_TEMPLATE_4524.tmpl_open_window();
		
		//notify 'core' that chat_window is open now 
		IKLAD_4524.notify_window_state_changed({state: 'open'});
		IKLAD_TEMPLATE_4524.chat_window_open = true;
		
		IKLAD_TEMPLATE_4524.scrol_msg_list_to_bottom();
	},
	
	close_chat_window: function (params) {
		IKLAD_TEMPLATE_4524.tmpl_close_window();
		
		//notify 'core' that chat_window is closed now 
		IKLAD_4524.notify_window_state_changed({state: 'closed'});
		IKLAD_TEMPLATE_4524.chat_window_open = false;
	},
	
	
	full_chat_log_data: function (params) {
		//params.msgs: array of 'msg_obj': (see operator_message function for description)
		
		IKLAD_TEMPLATE_4524.msgs_container.innerHTML = '';
		IKLAD_TEMPLATE_4524.msgs_count = 0;
		
		for (var i=0; i < params.msgs.length; i++) {
			IKLAD_TEMPLATE_4524.local_on_chat_message(params.msgs[i], false);
		};
	},
	
	on_chat_message: function (msg_obj) {
		// msg_obj: {
		//	type: msg || form					(text = form_id for [type=form])
		//	completed: 0 | 1   (ONLY FOR FORM)
		//  text: text of message	(already processed for smiles/html chars, so it's ready to 'display') OR form_id
		//  dt: datetime of message in format 'YYYY-MM-DD HH:MM:SS'
		//	to: 'client' || 'operator'
		//  id: internal id of msg
		//  is_info: 1|0  (1 = server info msg)
		//  operator_name: name of opertor who wrote this msg
		//  show_operator_name: 1|0 display operator name or not (set to 0 for welcome msg)
		//  by_human: 0|1   (1= wrote by human, 0=generated automatically by autioinitiate rule or in other way)
		// }
		
		IKLAD_TEMPLATE_4524.local_on_chat_message(msg_obj, true);
	},
	
	
	//
	__QF_cached_form_data: [],
	__QF_blink_field_error_count: 10,
		
	
	//form data callback by call to 'get_form_data'
	form_data: function (obj) {
		//obj.msg_id - id of message
		
		//obj.form_data::
		//form_data.ID - int
		
		//form_data.options = {}
		//form_data.options.display	 "modal", "top", "bottom", "inchat"
		
		
		//form_data.fields = []
		//form_data.fields ITEM: {
		//	ID: ...
		//	name: ...
		//	var_name: ...
		//	type: 'int', 'string', 'select', 'select-row', 'select-column', button   (+ SPECIAL:  'header' and 'title' )
		//	options: {
		//		required: 0|1
		//		lines: INT			(1 = input text,  >=2  - textarea)
		//		min_length: INT  (min input length)
		//		type: 		'submit', 'close_chat', 'close_form'  (for BUTTON)
		//	}
		//	default_value: 	'default value is here'
		//	values: [
		//		'value|display_value'    or only 'display_value'
		//		....
		//	]
		//}
		
		var CLASS_FOR_REPLACE = 'REPLACE_CLASS_4524';
		
		var js_call_prefix = (obj.form_data.options.display == 'inchat') ? 'parent.' : '';
		var rows = [];
		var cols = [];
		
		for (var i=0; i < obj.form_data.fields.length; i++) {
			var field = obj.form_data.fields[i];
			
			if (field.type == 'header') {
				rows.push(['<tr class="FORM_HEADER_4524 ' + CLASS_FOR_REPLACE + '">', '</tr>']);
				cols.push(['<td>', '<h1>' + field.name + '</h1>', '</td>']);
				continue;
			};
			
			if (field.type == 'title') {
				rows.push(['<tr class="FORM_TITLE_4524 ' + CLASS_FOR_REPLACE + '">', '</tr>']);
				cols.push(['<td>', '<h3>' + field.name + '</h3>', '</td>']);
				continue;
			};
			
			if (field.type == 'int') {
				if (field.name.length > 0) {
					rows.push(['<tr class="FORM_FIELD_TITLE_4524">', '</tr>']);
					cols.push([
					'<td>', 
						field.name,
					'</td>',
					]);
				};
				
				rows.push(['<tr class="FORM_FIELD_4524 FORM_FIELD_INT_4524 ' + CLASS_FOR_REPLACE + '">', '</tr>']);
				cols.push([
				'<td>', 
				'<input id="FORM_INPUT_4524_' + obj.form_data.ID + '_' + field.ID + '" type="text" name="' + field.var_name + '" value="' + field.value + '" orig_value="' + field.value + '" onfocus="' + js_call_prefix + 'IKLAD_TEMPLATE_4524.__form_el_focus(this, \'' + field.value + '\');" onblur="' + js_call_prefix + 'IKLAD_TEMPLATE_4524.__form_el_blur(this, \'' + field.value + '\');"' + '>', 
				'</td>'
				]);
				
				continue;
			};
			
			
			if (field.type == 'string') {
				if (field.name.length > 0) {
					rows.push(['<tr class="FORM_FIELD_TITLE_4524">', '</tr>']);
					cols.push([
					'<td>', 
						field.name,
					'</td>',
					]);
				};
				
				
				
				rows.push( ['<tr class="FORM_FIELD_4524 FORM_FIELD_STRING_4524 ' + CLASS_FOR_REPLACE + '">', '</tr>'] );
				
				var arr = ['<td>', '', '</td>'];
				
				if (field.options.lines == 1) {
					arr[1] = '<input id="FORM_INPUT_4524_' + obj.form_data.ID + '_' + field.ID + '" type="text" name="' + field.var_name + '" value="' + field.value + '" orig_value="' + field.value + '" onfocus="' + js_call_prefix + 'IKLAD_TEMPLATE_4524.__form_el_focus(this, \'' + field.value + '\');" onblur="' + js_call_prefix + 'IKLAD_TEMPLATE_4524.__form_el_blur(this, \'' + field.value + '\');"' + '>';
				} else {
					arr[1] = '<textarea id="FORM_INPUT_4524_' + obj.form_data.ID + '_' + field.ID + '" rows="' + field.options.lines + '" name="' + field.var_name + '" orig_value="' + field.value + '" onfocus="' + js_call_prefix + 'IKLAD_TEMPLATE_4524.__form_el_focus(this, \'' + field.value + '\');" onblur="' + js_call_prefix + 'IKLAD_TEMPLATE_4524.__form_el_blur(this, \'' + field.value + '\');"' + '>' + field.value + '</textarea>';
				};
				
				cols.push(arr);
				continue;
			};
			
			
			if (field.type == 'select') {
				if (field.name.length > 0) {
					rows.push(['<tr class="FORM_FIELD_TITLE_4524">', '</tr>']);
					cols.push([
					'<td>', 
						field.name,
					'</td>',
					]);
				};
				
				rows.push( ['<tr class="FORM_FIELD_4524 FORM_FIELD_SELECT_4524 ' + CLASS_FOR_REPLACE + '">', '</tr>'] );
				
				
				var select_el_html = '<select id="FORM_INPUT_4524_' + obj.form_data.ID + '_' + field.ID + '" name="' + field.var_name + '">';
				
				for (var k=0; k < field.values.length; k++) {
					var sel = '';
					
					var val, display_value;
					
					if (field.values[k].match(/^(.*?)\|(.*)/)) {
						val = RegExp.$1;
						display_value = RegExp.$2;
					} else {
						val = field.values[k];
						display_value = field.values[k];
					};
					
					if (field.default_value == val) {
						sel = 'selected';
					};
					
					select_el_html += '<option value="' + val + '"' + sel + ' >' + display_value + '</option>';
				};
				
				select_el_html += '</select>';
				
				
				cols.push(['<td>', select_el_html, '</td>']);
				continue;
			};
			
			
			if (field.type == 'select-column') {
				for (var k=0; k < field.values.length; k++) {
					//html += '<tr class="FORM_FIELD_4524 FORM_FIELD_SELECT_COL_4524 ' + CLASS_FOR_REPLACE + '"><td>';
					//html += '<div onclick="IKLAD_TEMPLATE_4524.__FormFieldSelectCol(' + obj.form_data.ID + ', ' + field.ID + ')" id="FORM_FIELD_SELECT_COL_4524_' + obj.form_data.ID + '_' + field.ID + '">' + field.values[k] + '</div>';
					//html += '</td></tr>';
				};
				continue;
			};
			
			
			if (field.type == 'button') {
				var this_btn_html = '<button id="FORM_BUTTON_4524_' + obj.form_data.ID + '_' + field.ID + '" name="' + field.var_name + '" value="' + field.value + '" onclick="' + js_call_prefix + 'IKLAD_TEMPLATE_4524.__QF_button_click(' + obj.form_data.ID + ', ' + obj.msg_id + ', \'' + field.options.type + '\')">' + field.name + '</button>';
				
				if ((field.options.on_prev_line == 1) && (cols.length > 0)) {
					rows[rows.length-1][0] = rows[rows.length-1][0].replace(CLASS_FOR_REPLACE, 'FORM_BUTTON_CONTAINER_4524 ' + CLASS_FOR_REPLACE);
					
					var col_html = field.options.html_container;
					col_html = col_html.replace(field.options.line_1_var, cols[cols.length-1][1]);
					col_html = col_html.replace(field.options.line_2_var, this_btn_html);
					cols[cols.length-1][1] = col_html;
					
				} else {
					rows.push( ['<tr class="FORM_BUTTON_CONTAINER_4524 ' + CLASS_FOR_REPLACE + '">', '</tr>'] );
					cols.push( ['<td colspan=2>', this_btn_html, '</td>'] );
				};

				continue;
			};
			

		};
		
		var html = '<table id="FORM_4524" cellpadding=0 cellspacing=0 style="width: 100%;">';
		for (var i=0; i < rows.length; i++) {
			rows[i][0] = rows[i][0].replace(CLASS_FOR_REPLACE, '');
			
			html += rows[i][0];
			
			for (var k=0; k < cols[i].length; k++) {
				html += cols[i][k];
			};
			
			html += rows[i][1];
		};
		html += '</table>';
		
		
		//save for future use
		IKLAD_TEMPLATE_4524.__QF_cached_form_data.push(obj);
		IKLAD_TEMPLATE_4524.__QF_show_form(obj.form_data.options.display, html, obj.msg_id);
	},
	
	
	
	send_form_data_result: function (result) {
		
		var frm_obj = IKLAD_TEMPLATE_4524.__QF_get_cached_form_data(result.form_id, result.msg_id);
		if (! frm_obj) return;
		
		var d = document;
		
		if (frm_obj.form_data.options.display == 'inchat') {
			d = IKLAD_TEMPLATE_4524.msgs_ifr.document;
		};
		
		
		if (result.result == 1) {
			
			for (var i = 0; i < result.cmd.length; i++) {
				var cmd = result.cmd[i];
				
				if (cmd.action == 'CLOSE_FORM') {
					IKLAD_TEMPLATE_4524.__QF_hide_form(frm_obj.form_data.options.display, result.form_id, result.msg_id);					
					IKLAD_4524.notify_form_completed(result.form_id, result.msg_id);
					continue;
				};
				
				if (cmd.action == 'CLOSE_CHAT') {
					IKLAD_TEMPLATE_4524.close_chat_window();
					IKLAD_4524.notify_form_completed(result.form_id, result.msg_id);
					continue;
				};
				
				if (cmd.action == 'FORM_ERROR') {
					var err_processed = false;
					
					if (cmd.error_type == 'field') {
						var field_id;
						
						var fields = d.querySelectorAll('*[id^="FORM_INPUT_4524_' + result.form_id + '_"]');
						
						for (var i=0; i < fields.length; i++) {
							if (fields[i].name == cmd.field) {
								field_id = fields[i].id;
								break;
							};
						};
						
						if (field_id) {
							err_processed = true;
							IKLAD_TEMPLATE_4524.__QF_blink_field_error(frm_obj.form_data.options.display == 'inchat' ? true : false, field_id, 'FORM_INPUT_ERROR_4524', true);
						};
					};
					
					if (! err_processed) alert(cmd.error_msg);
					
					
					//enable all buttons
					var btns = d.querySelectorAll('*[id^="FORM_BUTTON_4524_' + result.form_id + '_"]');
					
					for (var i=0; i < btns.length; i++) {
						var btn = btns[i];
						btn.className = '';
						btn.disabled = false;
					};
					
					continue;
				};
				
				
			};
			
		} else {
		};
	},
	

	
	__QF_get_cached_form_data: function (form_id, msg_id) {
		
		for (var i=0; i < IKLAD_TEMPLATE_4524.__QF_cached_form_data.length; i++) {
			if (! (IKLAD_TEMPLATE_4524.__QF_cached_form_data[i].msg_id == msg_id)) continue;
			if (! (IKLAD_TEMPLATE_4524.__QF_cached_form_data[i].form_data.ID == form_id)) continue;
			return IKLAD_TEMPLATE_4524.__QF_cached_form_data[i];
		};
		
	},
	
	__QF_button_click: function (form_id, msg_id, action) {
		var frm_obj = IKLAD_TEMPLATE_4524.__QF_get_cached_form_data(form_id, msg_id);
		if (! frm_obj) return;
		
		var d = document;
		
		if (frm_obj.form_data.options.display == 'inchat') {
			d = IKLAD_TEMPLATE_4524.msgs_ifr.document;
		};
		
		
		if ((action == 'submit') || (action == 'cancel')) {
			//disable all buttons
			var btns = d.querySelectorAll('*[id^="FORM_BUTTON_4524_' + form_id + '_"]');
			
			for (var i=0; i < btns.length; i++) {
				var btn = btns[i];
				btn.className = 'FORM_BUTTON_DISABLED_4524';
				btn.disabled = true;
			};
		};
		
		
		if (action == 'submit') {		//validatation of fields is NOT needed
			var data = 'action=submit';
			
			var fields = d.querySelectorAll('*[id^="FORM_INPUT_4524_' + form_id + '_"]');
			
			for (var i=0; i < fields.length; i++) {
				var field = fields[i];
				var orig_value = field.getAttribute('orig_value');
				
				if (orig_value && (orig_value == field.value)) {
					//do not send UNFILLED field
				} else {
					
					if (field.type == 'text') {
						data += '&' + field.name + '=' + escape(field.value);
					};
					
					if (field.type == 'select-one') {
						data += '&' + field.name + '=' + escape(field.value);
						data += '&' + field.name + '__TEXT=' + escape(field.options[field.selectedIndex].text);
					};
				};
			};
			
			IKLAD_4524.send_form_data(form_id, msg_id, data);
			return;
		};
		
		if (action == 'cancel') {
			IKLAD_4524.send_form_data(form_id, msg_id, 'action=cancel');
			return;
		};
		
		if (action == 'close_chat') {
			IKLAD_TEMPLATE_4524.close_chat_window();
			return;
		};
		
	},
	
	__QF_blink_field_error: function (in_iframe, el_id, el_class, flag) {
		var el
		
		if (in_iframe) {
			el = IKLAD_TEMPLATE_4524.msgs_ifr.document.getElementById(el_id);
		} else {
			el = document.getElementById(el_id);
		};
		
		if (! el) return;

		
		if (IKLAD_TEMPLATE_4524.__QF_blink_field_error_count-- <= 0) {
			IKLAD_TEMPLATE_4524.__QF_blink_field_error_count = 7; //reset
			el.className = el.className.replace(el_class, '');
			return;
		};
		
		if (flag) {
			el.className += ' ' + el_class;
		} else {
			el.className = el.className.replace(el_class, '');
		};
		
		var code = 'IKLAD_TEMPLATE_4524.__QF_blink_field_error(' + (in_iframe ? 'true' : 'false') + ',\'' + el_id + '\',\'' + el_class + '\',' + (flag ? 'false' : 'true') + ')';
		setTimeout(code, 100);
	},
	
	
	__QF_show_form: function (display, html, msg_id) {
		if (display == 'modal') {
			document.getElementById('MODAL_FORM_LAYER_CONTAINER_4524').innerHTML = html;
			IKLAD_TEMPLATE_4524.__show_layer('modal_form');
		};
		
		if (display == 'top') {
			IKLAD_TEMPLATE_4524.top_form_container.innerHTML = html;
			IKLAD_TEMPLATE_4524.top_form_container_tr.style.display = '';
		};
		
		if (display == 'bottom') {
			IKLAD_TEMPLATE_4524.bottom_form_container.innerHTML = html;
			IKLAD_TEMPLATE_4524.bottom_form_container_tr.style.display = '';
		};
		
		if (display == 'inchat') {
			var el = IKLAD_TEMPLATE_4524.msgs_ifr.document.getElementById('msg_' + msg_id);
			if (el) {
				el.innerHTML = html;
				el.style.display = '';
			};
			
			IKLAD_TEMPLATE_4524.scrol_msg_list_to_bottom();
		};
		
			try {
				    IKLAD_TEMPLATE_4524.scrol_msg_list_to_bottom();
			} catch (e) {};
		
	},
	
	__QF_hide_form: function (display, form_id, msg_id) {
		if (display == 'modal') {
			IKLAD_TEMPLATE_4524.__show_layer('default');
		};
		
		if (display == 'top') {
			IKLAD_TEMPLATE_4524.top_form_container_tr.style.display = 'none';
		};
		
		if (display == 'bottom') {
			IKLAD_TEMPLATE_4524.bottom_form_container_tr.style.display = 'none';
		};
		
		if (display == 'inchat') {
			var el = IKLAD_TEMPLATE_4524.msgs_ifr.document.getElementById('msg_' + msg_id);
			if (el) el.style.display = 'none';
		};
		
		try {
			    IKLAD_TEMPLATE_4524.scrol_msg_list_to_bottom();
		} catch (e) {};

		
	},
	
	
	
	
	
	
	//--------------------------------------------------------------------------------
	//--------------------------------------------------------------------------------
	//--------------------------------------------------------------------------------
	
	//LOCAL template functions/variables
	original_form_height: '',
	msgs_ifr: '',	//iframe variable holder
	msgs_container: '',	//msgs_container in iframe
	top_form_container: '',
	top_form_container_tr: '',
	bottom_form_container: '',
	bottom_form_container_tr: '',
	msgs_count: 0,
	operator_typing_container : '',
	operator_typing_msg_container: '',
	sound_enabled: true,
	chat_window_open: false,
	

	
	
	local_sound_on_off: function () {
		IKLAD_TEMPLATE_4524.sound_enabled = ! IKLAD_TEMPLATE_4524.sound_enabled;
		
		var img = document.getElementById('SOUND_ON_OFF_IMG_4524');
		
		if (IKLAD_TEMPLATE_4524.sound_enabled) {
			img.title = 'Звук включен';
			img.src = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAMCAYAAABr5z2BAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyBpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMC1jMDYwIDYxLjEzNDc3NywgMjAxMC8wMi8xMi0xNzozMjowMCAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNSBXaW5kb3dzIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjM4NUZGMDMzNjE1OTExRTA4RTM3QjFCRDY5NERFNTcwIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjM4NUZGMDM0NjE1OTExRTA4RTM3QjFCRDY5NERFNTcwIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6Mzg1RkYwMzE2MTU5MTFFMDhFMzdCMUJENjk0REU1NzAiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6Mzg1RkYwMzI2MTU5MTFFMDhFMzdCMUJENjk0REU1NzAiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz79Pb4QAAAAUUlEQVR42mLMaFvJgAM8BWJpBvzgPxMezVIMRAAmMjT/x2cA0TbDAAu6iXhsZSTWCySBwWEAIxJ+hkMdI7EukMZjCNFeIGQIIzFhQLRLAAIMAGl/DZkJirQ5AAAAAElFTkSuQmCC';
		} else {
			img.title = 'Звук выключен';
			img.src = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAMCAYAAABr5z2BAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA2RpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMC1jMDYwIDYxLjEzNDc3NywgMjAxMC8wMi8xMi0xNzozMjowMCAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDo4MTU5NzRDRjU4NjFFMDExODk0Q0UyQTExODBFNzkzOSIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo0RDEyQjQ5NDYxNTkxMUUwQTRGNDgwRDA5NTg2REVGOSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo0RDEyQjQ5MzYxNTkxMUUwQTRGNDgwRDA5NTg2REVGOSIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ1M1IFdpbmRvd3MiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDo4MzU5NzRDRjU4NjFFMDExODk0Q0UyQTExODBFNzkzOSIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDo4MTU5NzRDRjU4NjFFMDExODk0Q0UyQTExODBFNzkzOSIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PjhSMQEAAABNSURBVHjaYsxoW8mAAzydXhkmzUAAMOHSDMRSDEQAJko0YzOAJM0gwALE/xkoAEwMFILBYQAjEn5GqQukSTUEmxdIMgRXGBBtCECAAQCEYwv/JRgJSQAAAABJRU5ErkJggg==';
		};
	},
	
	
	
	
	
	
	local_run_file_upload_procedure: function (step) {
		var inp_f = document.getElementById('IKLAD_FILE_UPLOAD_INPUT_4524');
		
		if (step == 1) {
			inp_f.click();
			return;
		};

		if (inp_f.value == '') {
			//no msg to user
		} else {			
			document.IKLAD_FILE_UPLOAD_FORM_4524.cid.value = IKLAD_4524.client_id;
			document.IKLAD_FILE_UPLOAD_FORM_4524.submit();
			
			//emulate message
			IKLAD_TEMPLATE_4524.local_on_chat_message({
				"text": 'Загрузка файла начата' + ' ' + inp_f.value, 
				"to": "client", 
				"dt": "", 
				"id": 0, 
				"is_info": 1,
				"by_human": 0
			}, false);
		};
	},
	
	
	
	
	local_opinion_set: function (id, want_comment) {
		var comment = '';

		if (want_comment) {
			comment = prompt('Комментарии?');
		}; 

		IKLAD_4524.send_opinion(id, comment);
		IKLAD_TEMPLATE_4524.local_hide_opinion_dialog();
	},
	
	local_hide_opinion_dialog: function () {
		var H = document.getElementById('IKLAD_OPINION_BOX_4524');
		if (!H) return;
		H.style.left = H.style.top = '-2000px';
		H.style.display = 'none';
	},

	local_show_opinion_dialog: function (obj) {   // obj = show near obj (where clicked)
		var H = document.getElementById('IKLAD_OPINION_BOX_4524');
		if (!H) return;
		H.style.left = H.style.top = '-2000px';
		H.style.display = ''; //show it to offsetWidth/offsetHeight make work

		var Pos = IKLAD_FUNC.find_object_position(obj);
		Pos[0] = Pos[0] - H.offsetWidth + parseInt(obj.offsetWidth/2) + (window.pageXOffset || document.documentElement.scrollLeft);
		Pos[1] = Pos[1] - H.offsetHeight + parseInt(obj.offsetHeight/2) + (window.pageYOffset || document.documentElement.scrollTop);

		H.style.left = Pos[0] + 'px';
		H.style.top = Pos[1] + 'px';
	},
	
	
	
	
	local_send_chat_log_to_email: function () {
		var email = prompt('Email:');
		if (email) IKLAD_4524.send_chat_log_to_email(email);
	},
	
	
	
	local_on_chat_message: function (msg_obj, play_sound) {
		var e = IKLAD_TEMPLATE_4524.msgs_ifr.document.createElement('div');
		e.className = 'msg_line';
		e.id = 'msg_' + msg_obj.id;
		
		if (msg_obj.type == 'msg') {
			var line = '<table width=100% cellpadding=0 cellspacing=0>';
			
			var tm = '';
			if (msg_obj.dt.match(/ (\d\d?:\d\d):\d\d/)) {
				tm = RegExp.$1;
			};
			
			if (msg_obj.to == 'client') {
				
				//if (msg_obj.show_operator_name == '1') {
				//	line += msg_obj.operator_name + ':';
				//};
				
				line += '<tr>';
				line += '<td class="msg_from_operator_left"></td>';
				line += '<td class="msg_from_operator"><div class="msg_from_operator">' + msg_obj.text + '</div></td>';
				line += '<td class="msg_from_operator_time">' + tm + '</td>';
				line += '</tr>';
			} else {
				
				line += '<tr>';
				line += '<td class="msg_from_client_time">' + tm + '</td>';
				line += '<td class="msg_from_client"><div class="msg_from_client">' + msg_obj.text + '</div></td>';
				line += '<td class="msg_from_client_right"></td>';
				line += '</tr>';
			};
			
			line += '</table>';
			
			
			e.innerHTML = line;
		};
		
		if (msg_obj.type == 'form') {
			e.className += ' msg_line_form';
			e.style.display = 'none';
			if (msg_obj.completed == 1) {
				// do no show anything
			} else {
				IKLAD_4524.get_form_data(msg_obj.text, msg_obj.id);		// form_data  will be called as result
			};
		};
		
		
		IKLAD_TEMPLATE_4524.msgs_container.appendChild(e);
		IKLAD_TEMPLATE_4524.msgs_count++;
		IKLAD_TEMPLATE_4524.scrol_msg_list_to_bottom();
		
		if (IKLAD_TEMPLATE_4524.sound_enabled && IKLAD_TEMPLATE_4524.chat_window_open && play_sound) {
			IKLAD_4524.play_sound('new_message');
		};
	},
	
	scrol_msg_list_to_bottom: function () {
		var last_elem = IKLAD_TEMPLATE_4524.msgs_container.lastChild;
		
		if (IKLAD_TEMPLATE_4524.operator_typing_container.style.display != 'none') {
			last_elem = IKLAD_TEMPLATE_4524.operator_typing_msg_container;
		};
		
		if (last_elem) {
			var pos = IKLAD_FUNC.find_object_position(last_elem);
			IKLAD_TEMPLATE_4524.msgs_ifr.scrollTo(0, pos[1]);
		};
	},
	
	open_in_new_window: function () {
		var w = parseInt(document.getElementById('IKLAD_FLOAT_FORM_DIV_4524').offsetWidth);
		var h = parseInt(document.getElementById('IKLAD_FLOAT_FORM_DIV_4524').offsetHeight);
		
		IKLAD_TEMPLATE_4524.close_chat_window();
		IKLAD_4524.open_in_new_window({
			'width': w,
			'height': h
		});
	},
	

	draggable_initilized: false,	

	tmpl_open_window: function () {
		
		
		
		
		
		if (typeof IKLAD_TEMPLATE_4524.animate_window_open == 'function') {
		 IKLAD_TEMPLATE_4524.animate_window_open();
		} else {
			
		 		IKLAD_TEMPLATE_4524.std_window_open();
		 	
		};
		
		
		//this is required for IE
		if (navigator.appName.indexOf("Internet Explorer") != -1) {
			var parent = document.getElementById('IKLAD_MSGS_IFR_PARENT_4524');
			document.getElementById('IKLAD_MSGS_IFR_4524').height = parent.offsetHeight + 'px';
			
			parent = document.getElementById('IKLAD_TEXTAREA_ROW_4524');
			document.getElementById('IKLAD_TEXTAREA_4524').style.height = parseInt(parent.offsetHeight) + 'px';
		};
	},
	
	
	tmpl_close_window: function () {
		if (typeof IKLAD_TEMPLATE_4524.animate_window_close == 'function') {
		 IKLAD_TEMPLATE_4524.animate_window_close();
		} else {
		 IKLAD_TEMPLATE_4524.std_window_close();
		};
	},
	
	
	std_window_open: function (options) {
		var form_div = document.getElementById('IKLAD_FLOAT_FORM_DIV_4524');
		var new_style_display = '';
		
		try {
			if (typeof options == 'object') {
				var units = 'px';
				
				if (options.left) { 	
					if (options.left.match(/(px|%|em)$/)) { units = RegExp.$1; } else { units = 'px'; };
					form_div.style.left = parseInt(options.left) + units;
				};
				if (options.right) {
					if (options.right.match(/(px|%|em)$/)) { units = RegExp.$1; } else { units = 'px'; };
					form_div.style.right = parseInt(options.right) + units;
				};
				if (options.top) {
					if (options.top.match(/(px|%|em)$/)) { units = RegExp.$1; } else { units = 'px'; };
					form_div.style.top = parseInt(options.top) + units;
				};
				if (options.bottom) {
					if (options.bottom.match(/(px|%|em)$/)) { units = RegExp.$1; } else { units = 'px'; };
					form_div.style.bottom = parseInt(options.bottom) + units;
				};
				if (options.height) {
					if (options.height.match(/(px|%|em)$/)) { units = RegExp.$1; } else { units = 'px'; };
					form_div.style.height = parseInt(options.height) + units;
				};
				if (options.width) {
					if (options.width.match(/(px|%|em)$/)) { units = RegExp.$1; } else { units = 'px'; };
					form_div.style.width = parseInt(options.width) + units;
				};
				if (typeof(options.display) != 'undefined') {
					new_style_display = options.display;
				};
			};
		} catch (e) {};
		
		form_div.style.display = new_style_display;
	},
	
	std_window_close: function () {
		document.getElementById('IKLAD_FLOAT_FORM_DIV_4524').style.display = 'none';
	},
	

	
	
	
	
	animate_window_open: function () {
		if (typeof IKLAD_TEMPLATE_4524.get_chat_form_width_height == 'function') {
		 IKLAD_TEMPLATE_4524.get_chat_form_width_height();
		};
		
		
		
		
		  
			
			
		
		  
		     try {
		     	var btm = IKLAD_TEMPLATE_4524.form_height + parseInt($('#IKLAD_FLOAT_FORM_DIV_4524').css('margin-bottom'));
		      IKLAD_TEMPLATE_4524.std_window_open( { bottom: -1*btm + 'px' } );
		      $("#IKLAD_FLOAT_FORM_DIV_4524").stop(true).css({ 'bottom': -1*btm + 'px' }).animate({ "bottom": "0px" }, 600 );
		     } catch (e) {
		      IKLAD_TEMPLATE_4524.std_window_open( { bottom: '0px' } );
		     };
			
		
		  

		
		
	
	},

	animate_window_close: function () {
		try {
		 
		 
		  
			
			
		
		  
		  	 var btm = IKLAD_TEMPLATE_4524.form_height + parseInt($('#IKLAD_FLOAT_FORM_DIV_4524').css('margin-bottom'));
	       $("#IKLAD_FLOAT_FORM_DIV_4524").stop(true).animate({ "bottom": -1*btm + "px" }, 600, function(){
	          IKLAD_TEMPLATE_4524.std_window_close();
	          $("#IKLAD_FLOAT_FORM_DIV_4524").css({"bottom": "0px"});  //keep it back
	       });
			
		
		  
			
		
		 
		
		 } catch (e) {
		  IKLAD_TEMPLATE_4524.std_window_close();
		 };
	},
	
	
	

	
	
	
	form_height: 0,
	form_width: 0,
	form_width_height_set: false,
	
	get_chat_form_width_height: function () {
		if (IKLAD_TEMPLATE_4524.form_width_height_set) return;
		
		IKLAD_TEMPLATE_4524.form_width_height_set = true;
		
		var float_form = document.getElementById('IKLAD_FLOAT_FORM_DIV_4524');
		
	  if (float_form.style.display == '') {
			IKLAD_TEMPLATE_4524.form_height = float_form.offsetHeight;
			IKLAD_TEMPLATE_4524.form_width = float_form.offsetWidth;
	  } else {
	
	   var old_left = float_form.style.left;
	   var old_right = float_form.style.right;
	
	   if (old_left) {
	     float_form.style.left = '-10000px';
	     float_form.style.display = '';
	     IKLAD_TEMPLATE_4524.form_height = float_form.offsetHeight;
	     IKLAD_TEMPLATE_4524.form_width = float_form.offsetWidth;
	     float_form.style.display = 'none';
	     float_form.style.left = old_left;
	   };
	
	   if (old_right) {
	     float_form.style.right = '-10000px';
	     float_form.style.display = '';
	     IKLAD_TEMPLATE_4524.form_height = float_form.offsetHeight;
	     IKLAD_TEMPLATE_4524.form_width = float_form.offsetWidth;
	     float_form.style.display = 'none';
	     float_form.style.right = old_right;
	   };
	
	  };
	},
	
	
	
	
	__form_el_focus: function (el, def_text) {		
		if (el.value == def_text) {
			el.value = '';
			el.style.color = 'black';
		};
	},
	
	__form_el_blur: function (el, def_text) {
		if (el.value == '') {
			el.value = def_text;
			el.style.color = 'gray';
		};
	},
	
	
	
	textarea_prev_color: '',
	
	textarea_focus: function () {
		var t = document.getElementById('IKLAD_TEXTAREA_4524');
		
		if (t.value == 'Напишите ваше сообщение тут ...') {
			t.value = '';
			IKLAD_TEMPLATE_4524.textarea_prev_color = t.style.color;
			t.style.color = 'black';
		};
	},
	
	textarea_blur: function () {
		var t = document.getElementById('IKLAD_TEXTAREA_4524');
		
		if (t.value == '') {
			t.value = 'Напишите ваше сообщение тут ...';
			t.style.color = IKLAD_TEMPLATE_4524.textarea_prev_color;
		};
	},
	
	textarea_onkeydown: function (e) {
		if ((e.ctrlKey || e.altKey) && e.keyCode == 13) {
			document.getElementById('IKLAD_TEXTAREA_4524').value += "\n";
			try { if (e) e.preventDefault();} catch (er) {};
			return false;
		};
		
		if (e.keyCode == 13) {	// enter (w/o ctrl)
			IKLAD_TEMPLATE_4524.local_send_message();
			try { if (e) e.preventDefault();} catch (er) {};
			return false;
		};
		
		return true;
	},
	
	textarea_onkeypress: function () {
		IKLAD_TEMPLATE_4524.track_keyboard_activity();
	},
	
	local_send_message: function () {
		var t = document.getElementById('IKLAD_TEXTAREA_4524');
		
		if (t.value == '') return; //do not send empty msg
		if (t.value == 'Напишите ваше сообщение тут ...') return;	//do not send def text by clicking 'send btn'
		
		IKLAD_4524.send_message({'text': t.value});
		t.value = '';
		try { t.focus(); } catch (e) {};
	},
	
	
	
	//keyboard activity tracking
	keyboard_active: false,
	keyboard_activity_timeout_timer: '',
	last_send_keyboard_status: '',
	
	track_keyboard_activity: function () {
		var current_text = document.getElementById('IKLAD_TEXTAREA_4524').value;
		
		//obj.type == 'client_typing'			- operator keyboard activity
		//obj.status = 'composing' || 'paused' || ''				('' = clear status)
		
		if ((current_text == '') || (current_text == 'Напишите ваше сообщение тут ...')) {
			
			if (IKLAD_TEMPLATE_4524.keyboard_active || (IKLAD_4524.last_send_keyboard_status != '')) {
				IKLAD_4524.notify_client_activity({'type': 'client_typing', 'status': ''});
				IKLAD_4524.last_send_keyboard_status = '';
				IKLAD_TEMPLATE_4524.keyboard_active = false;
				
				clearTimeout(IKLAD_TEMPLATE_4524.keyboard_activity_timeout_timer);
				IKLAD_TEMPLATE_4524.keyboard_activity_timeout_timer = null;
			};
			
		} else {
			
			if (IKLAD_TEMPLATE_4524.keyboard_active) {
				//restart 'pause timeout' timer
				clearTimeout(IKLAD_TEMPLATE_4524.keyboard_activity_timeout_timer);
				IKLAD_TEMPLATE_4524.keyboard_activity_timeout_timer = setTimeout(IKLAD_TEMPLATE_4524.track_keyboard_activity_timeout, 5000);
			} else {
				//start
				IKLAD_4524.notify_client_activity({'type': 'client_typing', 'status': 'composing'});
				IKLAD_4524.last_send_keyboard_status = 'composing';
				IKLAD_TEMPLATE_4524.keyboard_active = true;
				IKLAD_TEMPLATE_4524.keyboard_activity_timeout_timer = setTimeout(IKLAD_TEMPLATE_4524.track_keyboard_activity_timeout, 5000);
			};
			
		};
	},
	
	track_keyboard_activity_timeout: function () {
		var current_text = document.getElementById('IKLAD_TEXTAREA_4524').value;
		
		clearTimeout(IKLAD_TEMPLATE_4524.keyboard_activity_timeout_timer);
		IKLAD_TEMPLATE_4524.keyboard_active = false;
		
		if ((current_text == '') || (current_text == 'Напишите ваше сообщение тут ...')) {
			IKLAD_4524.notify_client_activity({'type': 'client_typing', 'status': ''});
			IKLAD_4524.last_send_keyboard_status = '';
		} else {
			IKLAD_4524.notify_client_activity({'type': 'client_typing', 'status': 'paused'});
			IKLAD_4524.last_send_keyboard_status = 'paused';
		};
	}
	
};

		IKLAD_4524.TEMPLATE.HTML_CODE += '<!-- template design by:  zak.in.ua//at//gmail.com -->';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '<style type="text/css" id="IKLAD_CSS_4524">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '#IKLAD_FLOAT_FORM_DIV_4524, #IKLAD_FLOAT_FORM_DIV_4524 *, #IKLAD_OPINION_BOX_4524, #IKLAD_OPINION_BOX_4524 * {';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '  padding: 0;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '  margin: 0;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	border-spacing: 0;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	border-collapse: collapse;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	border: 0 none;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '  font-size: 11px;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '  line-height: normal !important;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '  vertical-align: top;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	text-align: left;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	text-indent: 0;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	text-decoration: none;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	outline: none;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	width: auto;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	min-width: 0;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	max-width: none;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	height: auto;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	min-height: 0;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	max-height: none;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	background: none;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	box-sizing: border-box;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	font-family: Tahoma;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	color: black;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '}';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '#IKLAD_FLOAT_FORM_DIV_4524 img {';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	display: inline;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '}';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '#IKLAD_TEXTAREA_4524, #IKLAD_SEND_BTN_CONTAINER_4524 {';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	background: -moz-linear-gradient(top, rgba(234,241,247,1) 0%, rgba(234,241,247,0) 22%); /* FF3.6+ */';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,rgba(234,241,247,1)), color-stop(22%,rgba(234,241,247,0))); /* Chrome,Safari4+ */';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	background: -webkit-linear-gradient(top, rgba(234,241,247,1) 0%,rgba(234,241,247,0) 22%); /* Chrome10+,Safari5.1+ */';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	background: -o-linear-gradient(top, rgba(234,241,247,1) 0%,rgba(234,241,247,0) 22%); /* Opera 11.10+ */';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	background: -ms-linear-gradient(top, rgba(234,241,247,1) 0%,rgba(234,241,247,0) 22%); /* IE10+ */';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	background: linear-gradient(to bottom, rgba(234,241,247,1) 0%,rgba(234,241,247,0) 22%); /* W3C */';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	filter: progid:DXImageTransform.Microsoft.gradient( startColorstr=\'#eaf1f7\', endColorstr=\'#00eaf1f7\',GradientType=0 ); /* IE6-9 */';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '}';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '#IKLAD_TEXTAREA_4524 {';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	resize: none; ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	overflow: auto; ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	width: 100% !important; ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	height: 100% !important; ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	border: 0; ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	padding: 3px 0 0 4px !important;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	outline: 0;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	font-size: 11px !important;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	box-shadow: none !important;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	font-weight: normal;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	box-sizing: border-box;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '}';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '#MODAL_FORM_LAYER_4524, #LOADING_LAYER_4524, #ONLINE_LAYER_4524 {';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	background-color: white;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '}';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '#CHAT_FORM_TITLE_4524, #FORM_4524 .FORM_HEADER_4524 h1  {';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	padding: 4px 2px; ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	font-weight: bold; ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	font-size: 14px; ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	color: #666666;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '}';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '#FORM_4524 .FORM_TITLE_4524 h3 {';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	padding: 4px; ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	color: #7a7a7a; ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	text-align: left; ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	min-height: 50px;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	font-weight: normal; ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '}';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '#FORM_4524 .FORM_FIELD_TITLE_4524 > td {';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	color: black;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	padding: 3px 4px;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '}';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '#FORM_4524 .FORM_FIELD_4524 > td {';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	padding: 2px 0;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '}';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '#FORM_4524 .FORM_FIELD_4524 input {';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	resize: none; ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	border: 1px solid #EBF1F8;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	outline: 0;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	width: 100%;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	font-size: 11px !important;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	padding-left: 4px !important;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	box-shadow: none !important;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	font-weight: normal !important;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	background: white;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	height: 23px !important;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '}';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '#FORM_4524 .FORM_FIELD_4524 input.FORM_INPUT_ERROR_4524 {';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	background: #EBF1F8;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '}';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '#FORM_4524 .FORM_FIELD_4524 textarea {';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	resize: none; ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	overflow: auto; ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	width: 100% !important; ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	height: 100% !important; ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	border: 0; ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	padding: 3px 0 0 4px !important;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	outline: 0;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	font-size: 11px !important;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	box-shadow: none !important;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	font-weight: normal;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '  background: white;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '  border: 1px solid #EBF1F8;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '  box-sizing: border-box;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '}';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '#FORM_4524 .FORM_FIELD_4524 textarea.FORM_INPUT_ERROR_4524 {';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	background: #EBF1F8;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '}';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '#FORM_4524 .FORM_BUTTON_CONTAINER_4524 > td {';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	padding: 2px 0 4px 0;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	text-align: center;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '}';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '#FORM_4524 .FORM_BUTTON_CONTAINER_4524 button {';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	color: black;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	border: 1px solid #f1f1f1;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	text-decoration: none;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	font-weight: bold;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	font-size: 12px;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	cursor: pointer;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	height: 23px !important;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	outline: none;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	padding: 0 4px;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	margin: 0 2px;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	background: #ebf1f8 none repeat scroll 0 0;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '}';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '#FORM_4524 .FORM_BUTTON_CONTAINER_4524 button.FORM_BUTTON_DISABLED_4524 {';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	color: gray;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '}';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '#IKLAD_HEADER_TD_4524 {';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	background: -moz-linear-gradient(top, rgba(216,228,240,0) 90%, rgba(216,228,240,1) 100%);';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	background: -webkit-gradient(linear, left top, left bottom, color-stop(78%,rgba(216,228,240,0)), color-stop(100%,rgba(216,228,240,1)));';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	background: -webkit-linear-gradient(top, rgba(216,228,240,0) 90%,rgba(216,228,240,1) 100%);';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	background: -o-linear-gradient(top, rgba(216,228,240,0) 90%,rgba(216,228,240,1) 100%);';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	background: -ms-linear-gradient(top, rgba(216,228,240,0) 90%,rgba(216,228,240,1) 100%);';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	background: linear-gradient(to bottom, rgba(216,228,240,0) 90%,rgba(216,228,240,1) 100%);';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	filter: progid:DXImageTransform.Microsoft.gradient( startColorstr=\'#00d8e4f0\', endColorstr=\'#d8e4f0\',GradientType=0 );';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '}';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '#IKLAD_OPINION_BOX_4524 {';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += ' position: absolute;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += ' background: none repeat scroll 0 0 #F7F7F7;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += ' border: 1px solid #D3DAE0;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += ' padding: 0;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += ' margin: 0;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '}';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '#IKLAD_OPINION_HEADER_4524 {';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += ' background-color: #EBF1F8;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '}';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '#IKLAD_OPINION_HEADER_4524 td {';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += ' font: 11px Tahoma; ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += ' padding: 0 3px 0 2px;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += ' border-bottom: 1px solid #D8DFE5;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += ' color: #45688E;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '}';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += 'td.IKLAD_OPINION_LIST_4524 {';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += ' padding-left: 4px !important;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += ' cursor: pointer !important;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += ' color: gray !important;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += ' font-size: 12px !important;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += ' text-decoration: none !important;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += ' text-align: left !important;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '}';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += 'td.IKLAD_OPINION_LIST_4524:hover {';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += ' color: black !important;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += ' text-decoration: underline !important;';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '}';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '</style>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '<div style="display: none;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '  <form action="//chat.iklad-chat.biz/file_upload.cgi" method="POST" enctype="multipart/form-data" target="upload_dst" name="IKLAD_FILE_UPLOAD_FORM_4524">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '   <input type="hidden" name="c" value="4524">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '   <input type="hidden" name="cid" value="">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '   <input type="file" name="file" id="IKLAD_FILE_UPLOAD_INPUT_4524" onchange="IKLAD_TEMPLATE_4524.local_run_file_upload_procedure(2)">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '  </form>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '  <iframe name="upload_dst" src="" style="height:0; width:0; display:none;"></iframe>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '</div>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '<table style="width:310px; display:none; background: #EBF1F8; border: 1px solid #b9b9b9; border-radius: 6px; z-index:2100000010;    position: fixed; left:0; bottom:0;   margin-bottom:0px; margin-left:5px;     " id="IKLAD_FLOAT_FORM_DIV_4524" valign=top>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	<tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '		<td style="height:360px;" id="IKLAD_SET_HEIGHT_TD_4524">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '            ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '            <table style="height:100%; width:100%;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                <tr style="height: 70px;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                    <td style=" border-bottom: 1px solid #c6d6e8;" id="IKLAD_HEADER_TD_4524">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                       <table style="width:100%; height: 100%;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                           <tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                               <td colspan=2 align=center valign=middle style="height: 7px; text-align: center;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                   <img id="IKLAD_HEADER_IMG_4524" style="padding-top: 3px;" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACYAAAAFCAYAAAApBZ42AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACVJREFUeNpi/A8EDIMQsOzatWswuouBcZAGGAMLEI9GJSkAIMAA9TQMYwk+AtgAAAAASUVORK5CYII="> ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                               </td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                           </tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                           ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                           <tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                               <td style="width:50px; padding: 0 5px 0 5px;" align=center valign=middle>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                               		<!--template must define [VAR_OPERATOR_PHOTO_MAX_LONGEST_SIDE] variable to automatically resize photo-->';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '																	';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                  <img style="" src="//chat.iklad-chat.biz/img/templates/design3/def_photo.png" id="IKLAD_OPERATOR_PHOTO_4524">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                               </td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                               ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                               <td style="width:100%; " valign=top>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                    <table style="height:100%; width:100%;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                        <tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                            <td style="padding: 6px 0 0 5px; font-size: 14px;" align=left valign=top>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                                <table style="padding-top: 2px;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                                		<tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                                			<td colspan=2 style="padding-left: 1px; font-size: 14px; color:#666666;" id="IKLAD_TITLE_TEXT_4524">&#1054;&#1073;&#1084;&#1077;&#1085;&#1103;&#1090;&#1100;&#32;&#81;&#73;&#87;&#73;&#32;&#1085;&#1072;&#32;&#66;&#105;&#116;&#99;&#111;&#105;&#110;</td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                                		</tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                                    <tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                                        <td style="width: 10px; padding-top: 3px;"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAASVJREFUeNpUkr1twzAUhBmBa2QKVenSyZ2KzOE6M3gFT5BGhUt16Vy5yAzaQeTjexRyxx/EMXAwKH13fO+gl+vPl2u/V+gDmvSwMWV1ktNDTNY9yxI1bsGi8w1+gz6hWbM5PQoMySnkeAom74Avu8a7b8kFtsNc6rAlB9CFDGmcgwWc49m3MWYlnJ/h6HYoNO0qM87fNExM1uM/TMVu0tDNkzcuCDgaYWljMLHCex2lBcjoBWMkJONQEmkoYH6CYeYuZAZWRyjmuiChXat6Mp/zdrIDe6aTKX0MjlRSS3pN5n6adR3gXvDiVq/ncrgl/ZkkVxgN3tDk4vFwA3wJNX3uI9QxU08mfEGjm691yR3/Z/bM6mAeCSeTRzpsRZMLYX4SvwIMAMzxjYuV11bYAAAAAElFTkSuQmCC" id="IKLAD_OP_STATUS_IMG_4524"></td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                                        <td valign=top align=left style="padding-left: 5px; color: gray; font-size: 14px;" id="IKLAD_OP_STATUS_TEXT_4524">онлайн</td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                                    </tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                                </table>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                            </td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                            <td align=right valign=top style="width:20px; padding-right: 10px;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                            	<table align=right>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                            		<tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                            			';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                            			<td style="padding: 0 3px 0 3px;" id="IKLAD_OPEN_CHAT_IN_NEW_WINDOW_ICON_4524">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                            				<a href="#" onclick="IKLAD_TEMPLATE_4524.open_in_new_window(); return false;" title="Открыть в новом окне"><img border=0 src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAICAYAAADED76LAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAGNJREFUeNp8jiEOwCAMRX/HFI7r4FBwbRBcB9EEW1LRZdnGnmryXvJLIgKl9y5jDDw57IgxUghhH1j0G7TWZBuoZGY455Bzhs2RPnmXpZRrRh+nWuunNM45J7z3SCm9pLIEGAAobC0//ht2BgAAAABJRU5ErkJggg=="></a>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                            			</td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                            			';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                            			<td style="padding: 0 0 0 3px;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                            				<a href="#" onclick="IKLAD_TEMPLATE_4524.close_chat_window(); return false;" title="Скрыть чат"><img border=0 src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAHCAYAAADam2dgAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAF1JREFUeNpiZGBgUAJiQQbc4B0TkHgMxH9wKACJP2YGEv+A+C8QC2BRBDLgCxOU8wbEQVPwBSrOwIQk+ACI/0PZ/6F8MGBGUvQXSvMC8XMg/oDLJ4xQ3zIiCwIEGABRYBNSjF3hxQAAAABJRU5ErkJggg=="></a>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                            			</td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                            		</tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                            	</table>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                               ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                               ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                            </td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                        </tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                    </table>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                               </td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                           </tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                       </table>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                    </td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                </tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                <tr style="height:100%;" id="LOADING_LAYER_4524">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                    <td valign=top style="padding: 0 10px;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	            				<table style="width: 100%; height: 100%;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	            					<tr style="height: 100%;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	            						<td style="text-align: center; vertical-align: middle;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	            							<img src="data:image/gif;base64,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" />';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	            						</td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	            					</tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	            				</table>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                    </td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                </tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                <tr style="height:100%; display: none;" id="MODAL_FORM_LAYER_4524">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                  <td valign=top style="height: 100%; padding: 0 8px;" id="MODAL_FORM_LAYER_CONTAINER_4524">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                  </td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                </tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                <tr style="height:100%; display: none;" id="ONLINE_LAYER_4524">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                	<td valign=top>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                  	<table style="height: 100%; width: 100%;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                  		<tr id="TOP_FORM_CONTAINER_TR" style="display: none;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '			            			<td style="padding: 2px 5px; border-bottom: 1px solid #dee1df;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '			            				<div id="TOP_FORM_CONTAINER" style=""></div>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '			            			</td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '			            		</tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '			            		';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                  		<tr style="height:100%;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '		                    <td valign=top style="background: white;" id="IKLAD_MSGS_IFR_PARENT_4524">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '		                    	<iframe name="IKLAD_MSGS_IFR_4524" id="IKLAD_MSGS_IFR_4524" frameborder="0" border="0" scrolling="auto" width="100%" height="100%" style="border:0px; padding: 0; margin: 0; overflow: auto; width: 100%; height: 100%;"></iframe>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '		                    </td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                  		</tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '			                 ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '			            		<tr id="BOTTOM_FORM_CONTAINER_TR" style="display: none;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '			            			<td style="padding: 2px 5px; border-top: 1px solid #dee1df;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '			            				<div id="BOTTOM_FORM_CONTAINER"></div>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '			            			</td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '			            		</tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                  	</table>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                	</td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                </tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                <tr style="height: 40px; display: none;" id="IKLAD_TEXTAREA_ROW_CONTAINER_4524">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                    <td style="border-top: 1px solid #c6d6e8; background: white;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                        <table style="height: 100%; width:100%;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                            <tr style="height: 100%;" id="IKLAD_TEXTAREA_ROW_4524"> ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                <td valign=top>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                	<textarea id="IKLAD_TEXTAREA_4524" style="color: gray;" onfocus="IKLAD_TEMPLATE_4524.textarea_focus();" onblur="IKLAD_TEMPLATE_4524.textarea_blur();" onkeydown="return IKLAD_TEMPLATE_4524.textarea_onkeydown(event);" onkeypress="IKLAD_TEMPLATE_4524.textarea_onkeypress();">Напишите ваше сообщение тут ...</textarea>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                </td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                <td style="width: 20px; vertical-align: middle;" align=center valign=middle id="IKLAD_SEND_BTN_CONTAINER_4524">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                	<a href="#" onclick="IKLAD_TEMPLATE_4524.local_send_message(); return false;" title="Отправить сообщение"><img border=0 src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAAOCAYAAAD0f5bSAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJhJREFUeNrkksEKwjAQRDehwWIvxb9Q8P9/RayebNJLTQ9NTCGEkQiBKrSkZwcGloXH7MIwAJSrYdCwxhCnDbLWkNb9NijpbyDvPbKhEAKUanG/XVeTijToZ4+ukxEkIcQqxMw4QsoHTZPL/qnYlSXtq+oL4pxTXR+Wk1L3nHtByfZTlXje8XRmi1SE5o6lbJoLfvdzvwUYAECXaQXsPcoJAAAAAElFTkSuQmCC"></a>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                                </td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                            </tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                        </table>      ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                    </td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                </tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                <tr style="height: 24px; ">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                   <td style="border-top: 1px solid #c6d6e8; vertical-align: middle;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                   ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                    <table style="width: 100%;">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                    	<tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                        <td style="padding-left: 5px; text-align: left;" valign=middle>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                        	';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                        </td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '												';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '									      <td style="width:28px; padding-left: 2px; text-align: center;" align=center id="IKLAD_LEAVE_OPINION_ICON_4524">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '									         <a href="#" onclick="IKLAD_TEMPLATE_4524.local_show_opinion_dialog(document.getElementById(\'IKLAD_OPINION_IMG_4524\')); return false;" title="Оставить отзыв"><img id="IKLAD_OPINION_IMG_4524" border=0 src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAKCAYAAACngj4SAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAUZJREFUeNpi/P//PwMuEF+x/v+C9gAGn6xlDFunRzPiUhdWtOr/w+cfwGx7Y3kGR1MVBk97ZbB688hZcAs05EUZWBjwgBsPX4PpNx++MuCzbGVvKJx/5MxDho0HrjM0zNgLt8jWSBZMHz73GLeFc9ac+Q9TiA/AfAYDNibyYAwDFlGzwTQTIxOYxmnh7LXnGE4sS4XzYUEDCrKuEndGBhLBv///IBaC4gkWdMgA2TJkNszFMEcgy+ECUmL8UBYwSEGWhXvogLkrd1xhIMYAYgCyw0DmoiSaZ68+Em3IyeVp8OAEBS+ywTDHoqtDBiywCIWFMSkAOS5hcVzas4MhNdgIpx4W5AhFDgpQCvV30ERJcfKSAgQdAUr6PaWeOBMVCyhcQYpgABYU2w/e/b/54E2Gkr5dcMtW9YXhNEhEgBseT/gAQIABACdUg1RxcUVhAAAAAElFTkSuQmCC"></a>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '									      </td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '									      ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '					';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '												';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '									      <td style="width:17px; padding-left: 8px; text-align: center;" align=center id="IKLAD_FILE_UPLOAD_ICON_4524">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '									          <a href="#" onclick="IKLAD_TEMPLATE_4524.local_run_file_upload_procedure(1); return false;" title="Загрузить файл"><img border=0 src="data:image/png;base64,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"></a>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '									      </td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '									      ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '					';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '												';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '									      <td style="width:17px; padding-left: 4px;text-align: center;" id="IKLAD_SEND_TO_EMAIL_ICON_4524">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '									         <a href="#" onclick="IKLAD_TEMPLATE_4524.local_send_chat_log_to_email(); return false;" title="Отправить логи чата на Email"><img border=0 src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAMCAYAAACEJVa/AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyBpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMC1jMDYwIDYxLjEzNDc3NywgMjAxMC8wMi8xMi0xNzozMjowMCAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNSBXaW5kb3dzIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOkY0OUU2MkQzNjE1NTExRTA4Rjk3QjQ4QTFCOUMxNzc1IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOkY0OUU2MkQ0NjE1NTExRTA4Rjk3QjQ4QTFCOUMxNzc1Ij4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6RjQ5RTYyRDE2MTU1MTFFMDhGOTdCNDhBMUI5QzE3NzUiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6RjQ5RTYyRDI2MTU1MTFFMDhGOTdCNDhBMUI5QzE3NzUiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz5gdBHRAAAAlElEQVR42qSSgQ2AIAwEC2EKB3MGHcEFdARn0L1kjdoiJgVLUGzSEFp6PB/MMG8HAHTQHt5FgPkBQSc369S/ho3LHs7TClbUuYBvAVK9zfpVUA5IICStCtIADyU3KL4VNQ+US8FpbtOAURQFE7lffE5BrhEpaxiBKSQHSLmab1HRFfRjkRIQsSl5nj3xubyv3/4UYACtJ3DsoGqr0AAAAABJRU5ErkJggg=="></a>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '									      </td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '									      ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '									      ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '									      ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '									      <td style="width:20px; padding-left: 5px; text-align: center;" align=center id="IKLAD_SOUND_ON_OFF_ICON_4524">';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '									        <a href="#" onclick="IKLAD_TEMPLATE_4524.local_sound_on_off(); return false;"><img title="Звук включен" id="SOUND_ON_OFF_IMG_4524" border=0 src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAMCAYAAABr5z2BAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyBpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMC1jMDYwIDYxLjEzNDc3NywgMjAxMC8wMi8xMi0xNzozMjowMCAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNSBXaW5kb3dzIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjM4NUZGMDMzNjE1OTExRTA4RTM3QjFCRDY5NERFNTcwIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjM4NUZGMDM0NjE1OTExRTA4RTM3QjFCRDY5NERFNTcwIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6Mzg1RkYwMzE2MTU5MTFFMDhFMzdCMUJENjk0REU1NzAiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6Mzg1RkYwMzI2MTU5MTFFMDhFMzdCMUJENjk0REU1NzAiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz79Pb4QAAAAUUlEQVR42mLMaFvJgAM8BWJpBvzgPxMezVIMRAAmMjT/x2cA0TbDAAu6iXhsZSTWCySBwWEAIxJ+hkMdI7EukMZjCNFeIGQIIzFhQLRLAAIMAGl/DZkJirQ5AAAAAElFTkSuQmCC"></a>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '									      </td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '									      ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '									      ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '									      <td style="width:5px;"></td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '									    </tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                    </table>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                    ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                   </td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '                </tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '            </table>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '            ';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '		</td>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '	</tr>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";IKLAD_4524.TEMPLATE.HTML_CODE += '</table>';
IKLAD_4524.TEMPLATE.HTML_CODE += "\n";
		
		
		
		IKLAD_4524.init();
	