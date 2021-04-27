//
//  HomeScreenView.swift
//  TSU-NBA-FANTASY
//
//  Created by Jachike Uzendu on 3/15/21.
//

import Foundation
import UIKit

// declaring protocol
//protocol HomescreenViewProtocol {
//    //declaring the functions in protocol
//    func setup()
//    func showSomething()
//    func hideSomething()
//}


protocol HomesScreenViewDelegateProtocol {

}

class HomeScreenView: UIView {
    //declare the labels
    var topPlayerNameLabel: UILabel
    var topPlayerPointLabel: UILabel
    var fakeButton: UIButton
    var page2Button: UIButton
    var page3Button: UIButton
    var page4Button: UIButton
    var page5Button: UIButton
    var delegate: HomesScreenViewDelegateProtocol
    
    init(frame: CGRect, delegate: HomesScreenViewDelegateProtocol) {
        // create instance of class label for topPlayerNameLabel
        self.topPlayerNameLabel = UILabel()
        // create instance of class label for topPlayerPointLabel
        self.topPlayerPointLabel = UILabel()
        
        //create instance of button for fakeButton
        self.fakeButton = UIButton(frame: CGRect(x: 50, y: 100, width: 100, height: 50))
        self.page2Button = UIButton(frame: CGRect(x: 240, y: 100, width: 100, height: 50))
        self.page3Button = UIButton(frame: CGRect(x: 50, y: 175, width: 100, height: 50))
        self.page4Button = UIButton(frame: CGRect(x: 240, y: 175, width: 100, height: 50))
        self.page5Button = UIButton(frame: CGRect(x: 145, y: 250, width: 100, height: 50))
        
        //set delegate for communication with viewController
        self.delegate = delegate
        
        //call super class initializer
        super.init(frame: frame)
        self.setUp()
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    //MARK: Private
    private func setUp() {
        // set background green
        self.backgroundColor = UIColor.blue
        
        // set button title
        self.fakeButton.setTitle("Next", for: .normal)
        self.page2Button.setTitle("Page 2", for: .normal)
        self.page3Button.setTitle("Page 3", for: .normal)
        self.page4Button.setTitle("Page 4", for: .normal)
        self.page5Button.setTitle("Page 5", for: .normal)
        //create tap gesture
        let tapGesture = UITapGestureRecognizer(target: self, action: #selector(fakeButtonTapped))
        // set tap to button
        self.fakeButton.addGestureRecognizer(tapGesture)
        self.fakeButton.backgroundColor = UIColor.orange
        self.page2Button.backgroundColor = UIColor.orange
        self.page3Button.backgroundColor = UIColor.orange
        self.page4Button.backgroundColor = UIColor.orange
        self.page5Button.backgroundColor = UIColor.orange
        
        self.addSubview(fakeButton)
        self.addSubview(page2Button)
        self.addSubview(page3Button)
        self.addSubview(page4Button)
        self.addSubview(page5Button)
    }
    
    
    //MARK: Actions
    @objc func fakeButtonTapped() {
    }
}
