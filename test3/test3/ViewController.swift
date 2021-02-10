//
//  ViewController.swift
//  test3
//
//  Created by Zyon Savery on 2/9/21.
//

import Cocoa

class ViewController: NSViewController {

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
    override var representedObject: Any? {
        didSet {
        // Update the view, if already loaded.
        }
    }
    
}

struct Responce: Codable {
    var results = MyResult
    let status: String
}

struct MyResult: Codable {
    let status : Int
    let message: String
    let results : Int
    let filter: [String]
    let leagues: [Int:String]
}

