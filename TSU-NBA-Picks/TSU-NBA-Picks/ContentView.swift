//
//  ContentView.swift
//  TSU-NBA-Picks
//
//  Created by Zyon Savery on 2/4/21.
//

import SwiftUI
import Foundation

struct ContentView: View {
    var body: some View {
        Text("Hello, world!")
        Button("LeaugeAPI"){fetchLeagueAPI()}
    }
    
    func fetchLeagueAPI(){
        let headers = [
            "x-rapidapi-key": "9ab5f1799cmsh27212c7d8f60efep17f457jsn395ab0f973b6",
            "x-rapidapi-host": "api-nba-v1.p.rapidapi.com"
        ]

        let request = NSMutableURLRequest(url: NSURL(string: "https://api-nba-v1.p.rapidapi.com/leagues/")! as URL,
                                                cachePolicy: .useProtocolCachePolicy,
                                            timeoutInterval: 10.0)
        request.httpMethod = "GET"
        request.allHTTPHeaderFields = headers

        let session = URLSession.shared
        let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
            if (error != nil) {
                print(error as Any)
            } else {
                let httpResponse = response as? HTTPURLResponse
                let bodyLeague = ["api":[
                    "status":200,
                    "message":"GET leagues/",
                    "results":6,
                    "filters":[],
                    "leagues":[
                        0:"africa",
                        1:"orlando",
                        2:"sacramento",
                        3:"standard",
                        4:"utah",
                        5:"vegas",
                        ]
                    ]
                print(httpResponse as Any)
                print(bodyLeague[leagues[i]])
            }
        })
        
        l
        ]
        

        dataTask.resume()
    }
    
    
    
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
