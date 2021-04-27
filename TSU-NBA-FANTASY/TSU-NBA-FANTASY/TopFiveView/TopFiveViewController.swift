//
//  TopFiveViewController.swift
//  TSU-NBA-FANTASY
//
//  Created by Jachike Uzendu on 4/23/21.
//

import Foundation
import UIKit

class TopFiveViewController: UIViewController {
    var topFiveView: TopFiveView!
    let topFiveViewModel: TopFiveViewModel
    
    init(frame: CGRect) {
        self.topFiveViewModel = TopFiveViewModel()
        super.init(nibName: nil, bundle: nil)
        self.topFiveView = TopFiveView(frame: frame, delegate: self)
        self.view = self.topFiveView
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}

extension TopFiveViewController: TopFiveViewDelegate {
    
}
