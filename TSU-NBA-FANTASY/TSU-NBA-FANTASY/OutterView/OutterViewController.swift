//
//  OutterViewController.swift
//  TSU-NBA-FANTASY
//
//  Created by Jachike Uzendu on 4/23/21.
//

import Foundation
import UIKit


struct MyResult {
    let playerId: Int
    let fisrtName: String
    let lastName: String
    let pos: String
    let teamID: String
    let points: Float
    let totReb: Float
    let assists: Float
    let steals: Float
    let blocks: Float
    let turnovers: Float
    let fantasyPoints: Float
    
    init(json: [String: Any]){
        playerId = json["playerId"] as? Int ?? 0
        fisrtName = json["fisrtName"] as? String ?? ""
        lastName = json["lastName"] as? String ?? ""
        pos = json["pos"] as? String ?? ""
        teamID = json["teamID"] as? String ?? ""
        points = json["points"] as? Float ?? 0
        totReb = json["totReb"] as? Float ?? 0
        assists = json["assists"] as? Float ?? 0
        steals = json["steals"] as? Float ?? 0
        blocks = json["blocks"] as? Float ?? 0
        turnovers = json["turnovers"] as? Float ?? 0
        fantasyPoints = json["fantasyPoints"] as? Float ?? 0
    }

}


class OutterViewController: UIViewController {
    var outterView: OutterView!
    let outterViewModel: OutterViewModel!
    var homeScreenViewController: HomeScreenViewController!
    var topFiveViewController: TopFiveViewController!
    var positionViewController: PositionViewController!
    
    init(frame: CGRect) {
        self.outterViewModel = OutterViewModel()
        super.init(nibName: nil, bundle: nil)
        self.outterView = OutterView(frame: frame, delegate: self, menuOptions: self.outterViewModel.options)
        self.view = self.outterView
        setupViewControllers()
        
    let jsonUrlString = "https://tsufansite.com/info.php"
    guard let url =  URL(string: jsonUrlString) else
        {return}
    
    URLSession.shared.dataTask(with: url){(data, responce, err) in
        guard let data = data else {return}
        let dataAsString = String(data: data, encoding: .utf8)
        //print(dataAsString)
        
        do{
            let json = try JSONSerialization.jsonObject(with: data, options: [.mutableContainers, .allowFragments])
            print(json)
            
        } catch let jsonErr{
        
            print("error serializing json: ", jsonErr)
        }
        
        
    }.resume()
        
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    //MARK: Private
    func setupViewControllers() {
        self.homeScreenViewController = HomeScreenViewController(frame: outterView.contentView.bounds)
        self.topFiveViewController = TopFiveViewController(frame: outterView.contentView.bounds)
        self.positionViewController = PositionViewController(frame: outterView.contentView.bounds)
        guard let homeOption = self.outterViewModel.options.first else {
            return
        }
        self.menuOptionSelected(option: homeOption)
    }
}


extension OutterViewController: OutterViewDelegate {
    func menuOptionSelected(option: String) {
        self.outterView.hideMenuOptions()
        let options = outterViewModel.options
        if options.first == option {
            self.outterView.showView(view: homeScreenViewController.view, title: option)
        } else if options[1] == option {
            self.outterView.showView(view: topFiveViewController.view, title: option)
        } else  if options.last == option {
            self.outterView.showView(view: positionViewController.view, title: option)
        }
    }
    
    func menuButtonTapped() {
        self.outterView.showMenuOptions()
    }
}
