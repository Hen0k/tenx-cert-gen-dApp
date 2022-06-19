import React, { useState } from 'react'
import Logout from './Logout'
import { FileUpload } from 'react-ipfs-uploader'


const NFTMetadata = (props) => {

	const [fileUrl, setFileUrl] = useState('')

  	return(<>
  		<Logout token={props.tokenRemover} />
  		<h1>hello admin</h1>
      <div className="mb-3">
        <FileUpload setUrl={setFileUrl} />
            FileUrl : <a
                href={fileUrl}
                target='_blank'
                rel='noopener noreferrer'
            >
                {fileUrl}
            </a>
        </div>
      <form>
        <h3>NFT metadata</h3>
        <div className="mb-3">
          <label>Item Name</label>
          <input
            type="text"
            className="form-control"
            placeholder="Enter Item Name"
            
          />
        </div>
        
        
        <div className="d-grid">
          <button 
            type="submit" 
            className="btn btn-primary"
            // onSubmit={onSubmit}
          >
            Submit
          </button>
        </div>
      </form>
  
  		
  		
		
		</>
	)
}

export default NFTMetadata;