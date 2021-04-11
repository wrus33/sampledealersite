(function(){
	if(window.EDM && window.EDM.edwpSync){return;}
	window.EDM = window.EDM || {}; window.EDM.edwpSync = window.EDM.edwpSync || {isLoaded: true};
	function getEDMCookie(key) { if (!key) { return null; } return decodeURIComponent(document.cookie.replace(new RegExp("(?:(?:^|.*;)\\s*" + encodeURIComponent(key).replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\=\s*([^;]*).*$)|^.*$"), "$1")) || null; }
	if(getEDMCookie('_edwpv')){document.cookie = "_edwpv=" + getEDMCookie('_edwpv') + " ; path=/; domain=www.autocentersnissan.com; expires=Wed, 09-Apr-2031 19:23:11 GMT; SameSite=Lax; ";} else {document.cookie = "_edwpv=c2eef314-05f6-43ac-a233-fa6f8f6dea51; path=/; domain=www.autocentersnissan.com; expires=Wed, 09-Apr-2031 19:23:11 GMT; SameSite=Lax; ";}
	if(getEDMCookie('_edwps')){document.cookie = "_edwps=" + getEDMCookie('_edwps') + " ; path=/; domain=www.autocentersnissan.com; expires=Sun, 11-Apr-2021 19:53:11 GMT; SameSite=Lax; ";} else {document.cookie = "_edwps=890435772008585711; path=/; domain=www.autocentersnissan.com; expires=Sun, 11-Apr-2021 19:53:11 GMT; SameSite=Lax; ";}
	window.EDM.edwpSync.isSynced = true;
})();
