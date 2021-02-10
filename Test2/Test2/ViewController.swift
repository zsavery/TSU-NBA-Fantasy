//
//  ViewController.swift
//  Test2
//
//  Created by Zyon Savery on 2/6/21.
//

import UIKit

class ViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        let url = "https://api-nba-v1.p.rapidapi.com/leagues/"
        getData(from: url)
    }

    private func getData(from url:String){
        let task = URLSession.shared.dataTask(with: URL(string: url)!, completionHandler:{ data, responce, error in
        
            guard let data = data, error == nil else{
                print("Something welt wrong: League!")
                return
            }
        
        //get data
            var result: Responce?
            do{
                result = try JSONDecoder().decode(Responce.self, from: data)
            }
            catch{
                print("Error converting League! \(error.localizedDescription)")
            }
            guard let json = result else{
                return
            }
        
            print(json.status)
            print(json.results.message)
            })
            task.resume()

    }


}
//Error
struct Responce: Codable {
    var results = MyResult()
    let status: String
}

struct MyResult: Codable {
    let status : Int
    let message: String
    let results : Int
    let filter: [String]
    let leagues: [Int:String]
}



//    override func viewDidLoad() {
//        super.viewDidLoad()
//        // Do any additional setup after loading the view.
//
//        // Specify the header
//        let headers = [
//            "x-rapidapi-key": "9ab5f1799cmsh27212c7d8f60efep17f457jsn395ab0f973b6",
//            "x-rapidapi-host": "api-nba-v1.p.rapidapi.com"
//        ]
//
//
//        // URL Request
//        let request = NSMutableURLRequest(url: NSURL(string:"https://api-nba-v1.p.rapidapi.com/leagues/")! as URL,
//                                          cachePolicy: .useProtocolCachePolicy,
//                                            timeoutInterval: 10.0)
//        // Set the request type
//        request.httpMethod = "GET"
//        request.allHTTPHeaderFields = headers
//
//        // Sprcify the body
//        let body = ["status":200,
//        "message":"GET leagues/",
//        "results":6,
//        "filters":[],
//        "leagues":[
//            0:"standard",
//            1:"africa",
//            2:"sacramento",
//            3:"vegas",
//            4:"utah",
//            5:"orlando",
//            ]
//        ] as [String:Any]
//
//
//
//
//
//        // Get the URLSession
//        let session = URLSession.shared
//
//        // Create the data task
//        let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
//            if (error != nil) {
//                print(error as Any)
//            } else {
//                let httpResponse = response as? HTTPURLResponse
//                print(httpResponse as Any)
//            }
//        })
//
//        // Fire off the data task
//        dataTask.resume()
//    }
//
//
//}
//
