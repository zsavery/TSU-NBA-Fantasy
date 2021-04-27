//
//  HomeScreenViewController.swift
//  TSU-NBA-FANTASY
//
//  Created by Jachike Uzendu on 3/15/21.
//

import Foundation
import UIKit

class HomeScreenViewController: UIViewController {
//    var homeScreenView: HomescreenViewProtocol?
    var homeScreenView: HomeScreenView!
    var secondScreen: HomeScreenViewController?
        
    init(frame: CGRect) {
        super.init(nibName: nil, bundle: nil)
        //ovverwite my view with my homeScreenView
        self.homeScreenView = HomeScreenView(frame: frame, delegate: self)
        self.view = self.homeScreenView
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
//    func doSomethings() {
//        homeScreenView?.setup()
//        homeScreenView?.showSomething()
//        homeScreenView?.hideSomething()
//    }
}

extension HomeScreenViewController: HomesScreenViewDelegateProtocol {
    func nextButtonTapped() {
        let screen2 = HomeScreenViewController(frame: self.view.bounds)
        screen2.view.backgroundColor = .gray
        self.secondScreen = screen2
        self.present(screen2, animated: true, completion: nil)
    }
    
    func top5PageButtonTapped() {
        let screen3 = HomeScreenViewController(frame: self.view.bounds)
        screen3.view.backgroundColor = .red
        self.secondScreen?.dismiss(animated: true, completion: {
            
        })
    }
    
    func positionPageButtonTapped(){
        
    }
}
